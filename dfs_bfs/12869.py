import sys
from itertools import permutations
from collections import deque


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        q = queue.popleft()

        if q[0] == 0 and q[1] == 0 and q[2] == 0:
            return visited[q[0]][q[1]][q[2]]

        for dx, dy, dz in permutations([1, 3, 9], 3):
            qx, qy, qz = max(q[0] - dx, 0), max(q[1] - dy, 0), max(q[2] - dz, 0)

            if visited[qx][qy][qz] == -1:
                visited[qx][qy][qz] = visited[q[0]][q[1]][q[2]] + 1
                queue.append((qx, qy, qz))


N = int(sys.stdin.readline().rstrip())
hp = list(map(int, sys.stdin.readline().split()))

if N < 3:
    hp += [0] * (3 - N)

_max = max(hp) + 1
visited = [[[-1] * _max for _ in range(_max)] for _ in range(_max)]
visited[hp[0]][hp[1]][hp[2]] = 0

print(bfs(hp[0], hp[1], hp[2]))