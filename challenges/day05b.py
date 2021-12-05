import functools
import itertools
import operator
import sys
from collections import Counter


def abs_inclusive_range(n: int):
    if n >= 0:
        return (v for v in range(n + 1))
    return (-v for v in range(-n + 1))


def generate_points(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    dx, dy = end[0] - start[0], end[1] - start[1]
    xs, ys = abs_inclusive_range(dx), abs_inclusive_range(dy)
    return [(start[0] + x, start[1] + y) for x, y in itertools.zip_longest(xs, ys, fillvalue=0)]


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
