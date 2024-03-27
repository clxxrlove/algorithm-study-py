import sys


def check(n, x, y):
    # horizon
    for dx in range(9):
        if board[y][dx] == n:
            return False

    # vertical
    for dy in range(9):
        if board[dy][x] == n:
            return False

    sx, sy = x - x % 3, y - y % 3

    for dx in range(sx, sx + 3):
        for dy in range(sy, sy + 3):
            if board[dy][dx] == n:
                return False

    return True


def backtracking(depth):
    if depth == len(zero):
        for y in range(9):
            for x in range(9):
                print(board[y][x], end='')
            print()
        exit()

    zx, zy = zero[depth]
    for n in range(1, 10):
        if board[zy][zx] == 0 and check(n, zx, zy):
            board[zy][zx] = n
            backtracking(depth + 1)
            board[zy][zx] = 0


board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
zero = []

for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            zero.append((x, y))

backtracking(0)