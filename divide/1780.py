# https://www.acmicpc.net/problem/1780
import sys

N = int(sys.stdin.readline().rstrip())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []


def divide(x, y, N):
    color = square[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != square[i][j]:
                for k in range(0, 3):
                    for l in range(0, 3):
                        divide(x + (N // 3 * k), y + (N // 3 * l), N // 3)
                return

    result.append(color)


divide(0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))