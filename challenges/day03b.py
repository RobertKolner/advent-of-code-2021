import sys
from collections import Counter


def run(values_str: str):
    bit_fields = [v.strip() for v in values_str.split("\n") if v]

    def filter_ratings(ratings: list[str], prefix="", most_significant_bit=True) -> str:
        if len(ratings) <= 1:
            return ratings[0]
        bit_counts = Counter(r[len(prefix)] for r in ratings).most_common(2)
        if bit_counts[0][1] == bit_counts[1][1]:
            prefix += "1" if most_significant_bit else "0"
        else:
            prefix += bit_counts[0][0] if most_significant_bit else bit_counts[1][0]
        return filter_ratings(
            [r for r in ratings if r.startswith(prefix)], prefix, most_significant_bit
        )

    oxy_ratings = filter_ratings(bit_fields, most_significant_bit=True)
    co2_ratings = filter_ratings(bit_fields, most_significant_bit=False)

    return int(oxy_ratings, 2) * int(co2_ratings, 2)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
