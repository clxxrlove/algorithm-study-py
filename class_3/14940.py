# https://www.acmicpc.net/problem/14940
import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

N, M = map(int, sys.stdin.readline().split())
sx, sy = 0, 0
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    if 2 in graph[i]:
        sx, sy = i, graph[i].index(2)

visited = [[False for _ in range(M)] for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]


def bfs(x, y, visited):
    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        q = queue.popleft()
        X, Y = q[0], q[1]
        tmp = result[X][Y]
        for a, b in ((X - 1, Y), (X + 1, Y), (X, Y - 1), (X, Y + 1)):
            if 0 <= a < N and 0 <= b < M and not visited[a][b]:
                if graph[a][b] == 1:
                    visited[a][b] = True
                    queue.append([a, b])
                    result[a][b] = tmp + 1
                    graph[a][b] = 0


bfs(sx, sy, visited)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            result[i][j] = -1

for r in result:
    print(*r)