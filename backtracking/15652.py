# https://www.acmicpc.net/problem/15652
import sys

N, M = map(int, sys.stdin.readline().split())
result = []


def backtracking():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if len(result) == 0 or result[-1] <= i:
            result.append(i)
            backtracking()
            result.pop()


backtracking()