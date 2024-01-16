# https://www.acmicpc.net/problem/2468
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = []
limit = max(map(max, graph))


def bfs(x, y, pivot, visited):
    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        q = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            qx, qy = q[0] + dx, q[1] + dy
            if 0 <= qx < N and 0 <= qy < N and not visited[qx][qy]:
                if graph[qx][qy] > pivot:
                    queue.append([qx, qy])
                    visited[qx][qy] = True


for pivot in range(limit):
    visited = [[False] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > pivot:
                bfs(i, j, pivot, visited)
                tmp += 1
    count.append(tmp)

print(max(count))