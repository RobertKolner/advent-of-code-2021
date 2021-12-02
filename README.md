# Advent of code 2021

Those are my solutions.
There are many like them, but these are mine.

## Installation

I assume you have [poetry](https://python-poetry.org/) already set up.

```shell
poetry install
```

If not, don't worry, a combination of pip and venv is also fine:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run a script for a single day, use:

```shell
poetry run ./fixtures.py <day> | poetry run python challenges/dayNNv
```

...or, without poetry:

```shell
./fixtures.py <day> | python challenges/dayNNv
```
