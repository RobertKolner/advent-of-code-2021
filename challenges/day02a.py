import sys


def run(values_str: str):
    lines = [v.strip().split(" ") for v in values_str.split("\n") if v]
    directions = [(line[0], int(line[1])) for line in lines]
    horizontals, depths = zip(
        *[(v, 0) if d == "forward" else (0, v) if d == "down" else (0, -v) for d, v in directions]
    )
    return sum(horizontals) * sum(depths)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
