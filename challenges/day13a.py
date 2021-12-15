import collections
import sys


def run(values_str: str):
    coordinate_bulk, instruction_bulk = values_str.split("\n\n")
    coordinates = {
        (int(line.split(",")[0]), int(line.split(",")[1]))
        for line in coordinate_bulk.split("\n")
        if line
    }
    instructions = [
        (line.split("=")[0].replace("fold along ", "").strip(), int(line.split("=")[1]))
        for line in instruction_bulk.split("\n")
        if line
    ]

    max_x = max(x for x, _ in coordinates) + 1
    max_y = max(y for _, y in coordinates) + 1

    for direction, xy in instructions:
        if direction == "x":
            coordinates = {(x if x < xy else max_x - x - 1, y) for x, y in coordinates if x != xy}
            max_x //= 2
        else:
            coordinates = {(x, y if y < xy else max_y - y - 1) for x, y in coordinates if y != xy}
            max_y //= 2
        break
    return len(coordinates)


if __name__ == "__main__":
    print(run(sys.stdin.read()))
