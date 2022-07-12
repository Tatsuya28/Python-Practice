import numpy as np


def check(y, x, k):
    a = 0 if y in [0, 1, 2] else 3 if y in [3, 4, 5] else 6
    b = 0 if x in [0, 1, 2] else 3 if x in [3, 4, 5] else 6
    return all(k not in p for p in [grid[y, :], grid[:, x], grid[a:a+3, b:b+3]])


def solve():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for k in range(1, 10):
                    if check(y, x, k):
                        grid[y][x] = k
                        if solve():
                            return True
                        grid[y][x] = 0
                return False
    return True


if __name__ == '__main__':
    grid = np.array([list(map(int, input())) for _ in range(9)])
    solve()
    for i in grid:
        print(''.join(map(str, i)))
