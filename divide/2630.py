# https://www.acmicpc.net/problem/2630
import sys

N = int(sys.stdin.readline().rstrip())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []


def divide(x, y, N):
    color = square[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != square[i][j]:
                divide(x, y, N // 2)
                divide(x, y + N // 2, N // 2)
                divide(x + N // 2, y, N // 2)
                divide(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


divide(0, 0, N)
print(result.count(0))
print(result.count(1))