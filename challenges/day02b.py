import sys


def run(values_str: str):
    lines = [v.strip().split(" ") for v in values_str.split("\n") if v]
    directions = [(line[0], int(line[1])) for line in lines]

    operations = {
        "down": lambda v, _: (0, 0, v),
        "up": lambda v, _: (0, 0, -v),
        "forward": lambda v, a: (v, a * v, 0),
    }

    aim = 0
    horizontal = 0
    depth = 0
    for d, v in directions:
        dh, dd, da = operations[d](v, aim)
        horizontal += dh
        depth += dd
        aim += da

    return horizontal * depth


if __name__ == "__main__":
    print(run(sys.stdin.read()))
