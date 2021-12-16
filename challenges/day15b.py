import heapq
import sys


def run(values_str: str):
    og_board = [[int(v) for v in line] for line in values_str.split("\n") if line]
    og_board_size = (len(og_board[-1]), len(og_board))

    def b(bx, by):
        v = og_board[by % og_board_size[1]][bx % og_board_size[0]]
        v += bx // og_board_size[0] + by // og_board_size[1]
        return v if v < 10 else v - 9

    end = (5 * og_board_size[0] - 1, 5 * og_board_size[1] - 1)
    queue = []
    heapq.heappush(queue, (0, (0, 0)))
    added_coords = set()

    while True:
        risk, coordinates = heapq.heappop(queue)

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = (coordinates[0] + dx, coordinates[1] + dy)
            if (x, y) == end:
                return risk + b(x, y)
            if (x, y) in added_coords:
                continue
            added_coords.add((x, y))
            if end[0] >= x >= 0 and end[1] >= y >= 0:
                heapq.heappush(queue, (risk + b(x, y), (x, y)))


if __name__ == "__main__":
    print(run(sys.stdin.read()))
