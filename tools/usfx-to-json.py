###############################################################################
#                                                                             #
# Copyright 2024 Evan Cox <evanacox00@gmail.com>. All rights reserved.        #
#                                                                             #
# Use of this source code is governed by a BSD-style license that can be      #
# found in the LICENSE.txt file at the root of this project, or at the        #
# following link: https://opensource.org/licenses/BSD-3-Clause                #
#                                                                             #
###############################################################################
#                                                                             #
# This file convers the ebible.org USFX format into the JSON format described #
# in docs/json-format.md. The JSON output is part of the website, and is used #
# for computing book/chapter/verse lengths when creating plans.               #
#                                                                             #
###############################################################################

import argparse
import xml.etree.ElementTree as et


Verse = dict[str, int | str]
Chapter = dict[str, int | list[Verse]]
Book = dict[str, str | list[Chapter]]


RawChapter = tuple[int, list[et.Element]]


def read_verses(chapter_contents: list[et.Element]) -> list[Verse]:
    #
    # I think the easiest way to make sense of all of this is to do a DFS
    # and linearize the contents of the chapter into one array, then split
    # based on <v> / <ve> tags for each verse
    #
    for child in chapter_contents:
        if child.tag == "q" or child.tag == "p":
            pass


def read_entire_book(book: et.Element) -> Book:
    name_abbrev = book.attrib["id"]

    #
    # the XML has a linear structure like this:
    #
    #   <book>
    #     ... bunch of metadata tags
    #     <c id=1 />
    #     <s>section title</s>
    #     <p>some text</p>
    #     <p>some text</p>
    #     <c id=2 />
    #     ....
    #   </book>
    #
    # we just read all the tags *between* each <c> tag to get all
    # the content for "one chapter", and then parse it from there to
    # get the actual verse contents
    #
    raw_chapters: list[RawChapter] = []

    for child in book:
        # once we hit a chapter, make a new list of tags
        if child.tag == "c":
            raw_chapters.append((child.attrib["id"], []))
        # this ignores the initial metadata and only gets the ones between chapters
        elif len(raw_chapters) != 0:
            raw_chapters[-1][1].append(child)

    # now that we've built up the above structure, we parse each individual chapter
    # into individual (and complete) chapters with their verses and whatnot
    chapters: list[Chapter] = []

    for chapter_num, elements in raw_chapters:
        print(f"    chapter '{chapter_num}'")
        chapters.append({
            "n": int(chapter_num),
            "verses": read_verses(elements)
        })

    return {
        "id": name_abbrev,
        "chapters": chapters
    }


def main():
    parser = argparse.ArgumentParser(
        prog="usfx-to-json", description="converts a USFX-foramt XML file into a JSON tree structure")

    parser.add_argument("filename")
    args = parser.parse_args()
    tree = et.parse(args.filename)

    books = []

    for child in tree.getroot():
        if child.tag == "book":
            print(f"book '{child.attrib["id"]}'")
            read_entire_book(child)


if __name__ == "__main__":
    main()
