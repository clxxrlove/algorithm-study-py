# https://www.acmicpc.net/problem/2667
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
_map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
_complex = []


def dfs(x, y):
    queue = deque([[x, y]])
    _map[x][y] = 0
    count = 1

    while queue:
        q = queue.popleft()
        qx, qy = q[0], q[1]

        for dx, dy in [(qx + 1, qy), (qx - 1, qy), (qx, qy + 1), (qx, qy - 1)]:
            if 0 <= dx < N and 0 <= dy < N and _map[dx][dy] == 1:
                    _map[dx][dy] = 0
                    queue.append([dx, dy])
                    count += 1

    return count


for i in range(N):
    for j in range(N):
        if _map[i][j] != 0:
            _complex.append(dfs(i, j))

print(len(_complex))
for c in sorted(_complex):
    print(c)