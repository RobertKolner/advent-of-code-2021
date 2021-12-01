#!/usr/bin/env python3
import os.path
import pathlib
import sys
from typing import Union

import requests

import config

cache_dir = pathlib.Path(os.path.dirname(__file__)) / ".fixtures"


def load(year: str, day: str) -> str:
    data = _load_from_cache(year, day)
    if data is None:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        session = config.env.aoc_session
        if session is None:
            raise ValueError("Session cannot be None")
        response = requests.get(url, cookies={"session": session})
        if response.status_code == 200:
            data = response.text
            _save_to_cache(year, day, data)
        else:
            raise Exception(
                f"Couldn't get input data (status code {response.status_code}: {response.text}"
            )
    return data


def _load_from_cache(year: str, day: str) -> Union[str, None]:
    cache_file = cache_dir / f"data_{year}_{day}.cache"
    try:
        with open(str(cache_file), "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


def _save_to_cache(year: str, day: str, data: str) -> None:
    os.makedirs(cache_dir, exist_ok=True)
    cache_file = cache_dir / f"data_{year}_{day}.cache"
    with open(str(cache_file), "w") as f:
        f.write(data)


if __name__ == "__main__":
    try:
        sys.stdout.write(load("2021", sys.argv[1]))
    except IndexError:
        sys.stderr.write(f"Usage: {sys.argv[0]} <day>\n")
