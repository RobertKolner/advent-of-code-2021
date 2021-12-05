import functools
import operator
import sys
from collections import Counter


def generate_points(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    start, end = sorted((start, end))
    dx, dy = end[0] - start[0], end[1] - start[1]
    if dx and dy:
        return []
    if dx:
        return [(x + start[0], start[1]) for x in range(dx + 1)]
    return [(start[0], y + start[1]) for y in range(dy + 1)]


def run(values_str: str):
    str_lines = [line.strip() for line in values_str.split("\n")]
    point_pairs = [
        tuple([int(v) for v in side.split(",")] for side in str_line.split(" -> "))
        for str_line in str_lines
        if str_line
    ]
    lines = [generate_points(*pair) for pair in point_pairs]
    counter = Counter(functools.reduce(operator.concat, lines))
    return sum(1 for _, count in counter.items() if count >= 2)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
