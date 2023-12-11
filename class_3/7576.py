# https://www.acmicpc.net/problem/7576
import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

result = 0
for g in graph:
    if 0 in g:
        print(-1)
        exit()
    result = max(max(g), result)

print(result - 1)