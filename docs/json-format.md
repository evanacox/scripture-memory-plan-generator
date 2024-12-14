# JSON Bible Format

This relies on the NET Bible to compute verse/chapter lengths. The format being consumed
looks like this:

```json
{
    "books": [
        {
            "id": "GEN",
            "chapters": [
                {
                    "n": 1,
                    "verses": [
                        {
                            "id": 1,
                            "text": "In the beginning God created the heavens and the earth."
                        },
                        // ...
                    ]
                },
                // ...
            ]
        },
        // ...
    ]
}
```

It uses the standard [Digital Bible Library USX Abbreviations](https://app.thedigitalbiblelibrary.org/static/docs/usx/vocabularies.html) for
book IDs.