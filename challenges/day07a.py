import sys


def run(values_str: str):
    positions = [int(v) for v in values_str.split(",") if v]
    return min(
        sum(abs(p - i) for p in positions) for i in range(min(positions), max(positions) + 1)
    )


if __name__ == "__main__":
    print(run(sys.stdin.read()))
