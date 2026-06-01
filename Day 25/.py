import numpy as np

def parse_input(input_str):
    lines = input_str.strip().splitlines()
    grid = np.array([[int(x) for x in line] for line in lines], dtype=int)
    return grid

def part1(grid):
    total_flashes = 0
    for step in range(100):
        grid += 1
        flashed = np.zeros_like(grid, dtype=bool)
        while True:
            new_flashes = (grid > 9) & ~flashed
            if not np.any(new_flashes):
                break
            flashed |= new_flashes
            for x, y in zip(*np.where(new_flashes)):
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                            grid[nx, ny] += 1
        total_flashes += np.sum(flashed)
        grid[flashed] = 0
    return total_flashes

def part2(grid):
    step = 0
    while True:
        step += 1
        grid += 1
        flashed = np.zeros_like(grid, dtype=bool)
        while True:
            new_flashes = (grid > 9) & ~flashed
            if not np.any(new_flashes):
                break
            flashed |= new_flashes
            for x, y in zip(*np.where(new_flashes)):
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                            grid[nx, ny] += 1
        if np.all(flashed):
            return step
        grid[flashed] = 0
if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    grid = parse_input(input_str)
    print("Part 1:", part1(grid.copy()))
    print("Part 2:", part2(grid.copy()))

