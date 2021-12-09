import sys


def run(values_str: str):
    records = [
        [
            [number.strip() for number in segment.split(" ") if number.strip()]
            for segment in line.split("|")
            if segment.strip()
        ]
        for line in values_str.split("\n")
        if line.strip()
    ]

    return sum(1 for record in records for number in record[1] if len(number) in {2, 3, 4, 7})


if __name__ == "__main__":
    print(run(sys.stdin.read()))
