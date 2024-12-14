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
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser(
        prog="usfx-to-json", description="converts a USFX-foramt XML file into a JSON tree structure")

    parser.add_argument("filename")
    args = parser.parse_args()
    tree = ET.parse(args.filename)

    for child in tree.getroot():
        print(f"child '{child.tag}' with value '{child.attrib}'")


if __name__ == "__main__":
    main()
