# https://www.acmicpc.net/problem/1074
import sys

N, R, C = map(int, sys.stdin.readline().split())
result = 0


def divide(x, y, N):
    global result
    if N > 1:
        if x <= R < x + 2 ** (N - 1):
            if y <= C < y + 2 ** (N - 1):
                divide(x, y, N - 1)
            else:
                result += 2 ** (2 * (N - 1))
                divide(x, y + 2 ** (N - 1), N - 1)
        else:
            result += (2 ** (2 * (N - 1))) * 2
            if y <= C < y + 2 ** (N - 1):
                divide(x + 2 ** (N - 1), y, N - 1)
            else:
                result += 2 ** (2 * (N - 1))
                divide(x + 2 ** (N - 1), y + 2 ** (N - 1), N - 1)
    else:
        for i in range(2):
            for j in range(2):
                sx, sy = x + i, y + j
                if sx == R and sy == C:
                    print(result)
                    exit(0)
                result += 1


divide(0, 0, N)