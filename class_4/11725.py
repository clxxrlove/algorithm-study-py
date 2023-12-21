# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(graph, i, visited)


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = [0] * (N + 1)

for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


dfs(graph, 1, visited)
for i in range(2, N + 1):
    print(result[i])