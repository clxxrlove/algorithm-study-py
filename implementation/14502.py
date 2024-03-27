import sys
from collections import deque


def deepcopy(arr):
    return [item[:] for item in arr]


def bfs():
    global answer

    q = deque(virus)
    _map = deepcopy(graph)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if _map[ny][nx] == 0:
                    _map[ny][nx] = 2
                    q.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0:
                count += 1

    answer = max(answer, count)


def wall(n):
    if n == 3:
        bfs()
        return

    for i in range(N): # y
        for j in range(M): # x
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(n + 1)
                graph[i][j] = 0


N, M = map(int, sys.stdin.readline().split()) # y, x
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((j, i))

answer = 0
wall(0)

print(answer)