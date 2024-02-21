import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
_map = [[0] * N for _ in range(N)]
_map[0][0] = 1

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    _map[x - 1][y - 1] = 2

L = int(sys.stdin.readline().rstrip())
d_info = dict()

for _ in range(L):
    X, C = sys.stdin.readline().split()
    d_info[int(X)] = C

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)] # x, y, 동 남 서 북
d, td, ans, t_time = 0, 0, 0, 0
hx, hy = 0, 0
tail = deque()
tail.append((0, 0))

while True:
    if ans in d_info:
        if d_info[ans] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

    ans += 1
    dx, dy = hx + direction[d][0], hy + direction[d][1]

    if 0 <= dx < N and 0 <= dy < N and _map[dy][dx] != 1:
        hx, hy = dx, dy
    else:
        print(ans)
        break

    if _map[dy][dx] == 2:
        tail.append((hx, hy))
        _map[dy][dx] = 1
    else:
        _map[dy][dx] = 1
        tail.append((hx, hy))
        tx, ty = tail.popleft()
        _map[ty][tx] = 0