import sys


def run(values_str: str):
    lines = [v.strip().split(" ") for v in values_str.split("\n") if v]
    directions = [(line[0], int(line[1])) for line in lines]

    aim = 0
    horizontal = 0
    depth = 0
    for d, v in directions:
        if d == "down":
            aim += v
        elif d == "up":
            aim -= v
        else:
            horizontal += v
            depth += aim * v

    return horizontal * depth


if __name__ == "__main__":
    print(run(sys.stdin.read()))
