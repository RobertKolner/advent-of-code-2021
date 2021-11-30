import os

import dotenv

dotenv.load_dotenv()


class _Config:
    def __init__(self):
        self.aoc_session = os.getenv("AOC_SESSION")


env = _Config()

__all__ = ["env"]
