# https://www.acmicpc.net/problem/2606
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
result = 0
for v in visited:
    if v: result += 1

print(result - 1)