# https://www.acmicpc.net/problem/10026
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited_rg_b = [[False] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs_rg_b(x: int, y: int, color, graph):
    queue = deque([[x, y]])
    visited_rg_b[x][y] = True

    while queue:
        q = queue.popleft()
        sx, sy = q[0], q[1]

        for dx, dy in direction:
            rx, ry = sx + dx, sy + dy
            if 0 <= rx < N and 0 <= ry < N and not visited_rg_b[rx][ry]:
                if color == graph[rx][ry]:
                    visited_rg_b[rx][ry] = True
                    queue.append([rx, ry])
                else:
                    if color in ["R", "G"] and graph[rx][ry] in ["R", "G"]:
                        visited_rg_b[rx][ry] = True
                        queue.append([rx, ry])


def bfs(x: int, y: int, color, graph):
    queue = deque([[x, y]])
    visited_rg_b[x][y] = True

    while queue:
        q = queue.popleft()
        sx, sy = q[0], q[1]

        for dx, dy in direction:
            rx, ry = sx + dx, sy + dy
            if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry]:
                if color == graph[rx][ry]:
                    visited[rx][ry] = True
                    queue.append([rx, ry])


ans_rg_b = 0
ans = 0

for i in range(N):
    for j in range(N):
        if not visited_rg_b[i][j]:
            bfs_rg_b(i, j, graph[i][j], graph)
            ans_rg_b += 1
        if not visited[i][j]:
            bfs(i, j, graph[i][j], graph)
            ans += 1

print(ans, ans_rg_b)