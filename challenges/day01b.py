def run(values_str: str):
    values = [int(v) for v in values_str.split("\n") if v]
    sums = [a + b + c for a, b, c in zip(values, values[1:], values[2:])]
    return sum(1 if b > a else 0 for a, b in zip(sums, sums[1:]))
