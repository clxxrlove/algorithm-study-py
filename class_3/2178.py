# https://www.acmicpc.net/problem/2178
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]


def bfs(x, y):
    q = deque([[x, y, 1]])
    result = 1

    while q:
        v = q.popleft()
        qx, qy, qd = v[0], v[1], v[2]

        for dx, dy in [(qx - 1, qy), (qx + 1, qy), (qx, qy - 1), (qx, qy + 1)]:
            if 0 <= dx < N and 0 <= dy < M and maze[dx][dy] == 1:
                maze[dx][dy] = 0
                q.append([dx, dy, qd + 1])

                if dx == N - 1 and dy == M - 1:
                    return qd + 1


ans = bfs(0, 0)
print(ans)