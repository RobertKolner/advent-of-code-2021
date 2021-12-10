import collections
import functools
import operator
import sys


def run(values_str: str):
    heightmap = [[int(v) for v in line] for line in values_str.split("\n") if line]
    basin_tiles = {
        (y, x) for y, line in enumerate(heightmap) for x, value in enumerate(line) if value < 9
    }
    basin_indexes = {}
    next_index = 1

    def flood(y, x, index):
        basin_indexes[(y, x)] = index
        basin_tiles.remove((y, x))
        for neighbor in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if neighbor in basin_tiles:
                flood(*neighbor, index)

    while len(basin_tiles) > 0:
        tile = next(iter(basin_tiles))
        flood(*tile, next_index)
        next_index += 1

    basin_sizes = collections.Counter(v for v in basin_indexes.values())
    return functools.reduce(operator.mul, (v for _, v in basin_sizes.most_common(3)), 1)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
