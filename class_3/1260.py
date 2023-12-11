# https://www.acmicpc.net/problem/14940
import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visitedD = [False] * (N + 1)
visitedB = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        q = queue.popleft()
        print(q, end=" ")
        for i in sorted(graph[q]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)


dfs(graph, V, visitedD)
print()
bfs(graph, V, visitedB)