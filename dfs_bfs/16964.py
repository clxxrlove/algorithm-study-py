# https://www.acmicpc.net/problem/16964
import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

judge = deque(list(map(int, sys.stdin.readline().split())))
order = []
visited = [False] * (N + 1)


def dfs(judge):
    for j in range(len(judge) - 1):
        visited[judge[j]] = True
        if judge[j + 1] in graph[judge[j]]:
            continue
        for g in graph[judge[j]]:
            if not visited[g]:
                return 0
    return 1


if judge[0] != 1:
    print(0)
    exit(0)

print(dfs(judge))