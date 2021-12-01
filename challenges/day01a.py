import sys


def run(values_str: str):
    values = [int(v) for v in values_str.split("\n") if v]
    return sum(1 if b > a else 0 for a, b in zip(values, values[1:]))


if __name__ == "__main__":
    print(run(sys.stdin.read()))
