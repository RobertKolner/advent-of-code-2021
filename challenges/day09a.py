import sys


def run(values_str: str):
    heightmap = [[int(v) for v in line] for line in values_str.split("\n") if line]
    risk_level = 0
    for row, _ in enumerate(heightmap):
        for col, value in enumerate(heightmap[row]):
            row_boundary = (row == 0 or heightmap[row - 1][col] > value) and (
                row == len(heightmap) - 1 or heightmap[row + 1][col] > value
            )
            col_boundary = (col == 0 or heightmap[row][col - 1] > value) and (
                col == len(heightmap[row]) - 1 or heightmap[row][col + 1] > value
            )
            if row_boundary and col_boundary:
                risk_level += 1 + value
    return risk_level


if __name__ == "__main__":
    print(run(sys.stdin.read()))
