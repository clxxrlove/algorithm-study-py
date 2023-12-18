# https://www.acmicpc.net/problem/15650
import sys

N, M = map(int, sys.stdin.readline().split())
result = []


def backtracking(s):
    if len(result) == M:
        print(*result)
        return

    for i in range(s, N + 1):
        if i not in result:
            result.append(i)
            backtracking(i + 1)
            result.pop()


backtracking(1)