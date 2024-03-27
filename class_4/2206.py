import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # y, x
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

queue = deque()
queue.append((0, 0, 1, 0))

visited = [[[4e9, 4e9] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
visited[0][0][1] = 1
# visited 더 파야함 -> 벽 판 경우, 안 판 경우에 최소값을 구해야함
while queue:
    qx, qy, dist, checked = queue.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = qx + dx, qy + dy

        if 0 <= nx < M and 0 <= ny < N:
            if nx == M - 1 and ny == N - 1:
                visited[ny][nx][checked] = min(visited[ny][nx][checked], dist + 1)
                continue

            if checked and graph[ny][nx] == 0:
                if dist < visited[ny][nx][checked]:
                    queue.append((nx, ny, dist + 1, checked))
                    visited[ny][nx][checked] = dist
                continue

            if not checked:
                if graph[ny][nx] == 0:
                    if dist < visited[ny][nx][0]:
                        queue.append((nx, ny, dist + 1, 0))
                        visited[ny][nx][0] = dist
                else:
                    if dist < visited[ny][nx][1]:
                        queue.append((nx, ny, dist + 1, 1))
                        visited[ny][nx][1] = dist

answer = min(visited[N - 1][M - 1])
print(answer if answer != 4e9 else - 1)