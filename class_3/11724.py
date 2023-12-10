# https://www.acmicpc.net/problem/11399
import sys
sys.setrecursionlimit(10 ** 7)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
conn = 0
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


for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        conn += 1

print(conn)