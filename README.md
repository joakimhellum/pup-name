# `pup-name`

A simple library and CLI tool for generating and validating pup names. [RFC1178](https://datatracker.ietf.org/doc/html/rfc1178) but for pups. 

## Features

* Generate pup names composed of adverbs, adjectives, and a noun (`pup`).
* Validate whether a pup name conforms to the expected format.
* Optionally append a short UUID suffix to ensure uniqueness.
* Command-line interface for your convenience.

## Installation

```sh
pip install pup-name
```

## Usage

Generate one pup name:

```sh
pup-name generate
```

Generate multiple pup names:

```sh
pup-name generate --words 3 --separator "-" --count 5
```

Validate a pup name:

```sh
pup-name validate rarely-right-pup
```

Python:

```python
from pup_name import generate, validate

name = generate(3, separator="-")
print(f"Generated pup name: {name}")

is_valid = validate(name, separator="-")
print(f"Is the name valid? {'Yes' if is_valid else 'No'}")
```
