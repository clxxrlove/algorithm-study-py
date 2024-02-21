import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())  # y, x
start_y, start_x, start_d = map(int, sys.stdin.readline().split())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # x, y, 북 동 남 서
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
visited = [[False for _ in range(M)] for _ in range(N)]
ans = 0


def solution(x, y, d):
    global ans
    q = deque([(x, y)])
    visited[y][x] = True
    ans += 1

    while q:
        sx, sy = q.popleft()
        flag = 0

        for _ in range(4):
            d = (d + 3) % 4
            dx, dy = sx + direction[d][0], sy + direction[d][1]

            if 0 <= dx < M and 0 <= dy < N and not _map[dy][dx] and not visited[dy][dx]:
                visited[dy][dx] = True
                q.append((dx, dy))
                ans += 1
                flag = 1
                break

        if flag == 0:
            if _map[sy - direction[d][1]][sx - direction[d][0]] != 1:
                q.append((sx - direction[d][0], sy - direction[d][1]))
            else:
                print(ans)
                exit()


solution(start_x, start_y, start_d)