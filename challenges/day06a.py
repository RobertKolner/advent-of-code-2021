import sys


def run(values_str: str):
    ages = [int(v) for v in values_str.split(",") if v]

    for _ in range(80):
        new_individuals = [8 for age in ages if age == 0]
        ages = [age - 1 if age > 0 else 6 for age in ages]
        ages.extend(new_individuals)
    return len(ages)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
