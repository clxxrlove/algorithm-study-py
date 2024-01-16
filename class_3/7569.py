import sys
from collections import deque

N, M, H = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(M)] for _ in range(H)]
visited = [[[False] * N for _ in range(M)] for _ in range(H)]
queue = deque()

for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 1:
                visited[i][j][k] = True
                queue.append([i, j, k])

while queue:
    z, y, x = queue.popleft()
    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        qx, qy, qz = x + dx, y + dy, z + dz

        if 0 <= qx < N and 0 <= qy < M and 0 <= qz < H and not visited[qz][qy][qx]:
            if box[qz][qy][qx] != -1:
                visited[qz][qy][qx] = True
                box[qz][qy][qx] = box[z][y][x] + 1
                queue.append([qz, qy, qx])

ans = 0
for ts in box:
    for t in ts:
        ans = max(ans, max(t))
        if 0 in t:
            print(-1)
            exit(0)

print(ans - 1)