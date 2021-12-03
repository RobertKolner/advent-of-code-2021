import sys
from collections import Counter


def run(values_str: str):
    bit_fields = [v.strip() for v in values_str.split("\n") if v]
    gamma_bits = [
        Counter(b[index] for b in bit_fields).most_common(1)[0][0]
        for index, _ in enumerate(bit_fields[0])
    ]
    epsilon_bits = ["1" if g == "0" else "0" for g in gamma_bits]
    return int("".join(gamma_bits), 2) * int("".join(epsilon_bits), 2)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
