# https://www.acmicpc.net/problem/15649
import sys

N, M = map(int, sys.stdin.readline().split())
result = []
visited = [False] * 100


def backtracking(N, M):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if i not in result:
            result.append(i)
            backtracking(N, M)
            result.pop()


backtracking(N, M)