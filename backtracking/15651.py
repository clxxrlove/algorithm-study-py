# https://www.acmicpc.net/problem/15650
import sys

N, M = map(int, sys.stdin.readline().split())
result = []


def backtracking():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        backtracking()
        result.pop()


backtracking()