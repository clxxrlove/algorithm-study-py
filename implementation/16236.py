import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark = [-1, -1]
level, exp = 2, 0

for y in range(N):
    for x in range(N):
        if _map[y][x] == 9:
            shark[0], shark[1] = x, y
            break


def bfs(x, y, size):
    q = deque([(x, y, 0)])
    visited = set()
    visited.add((x, y))
    result = []

    while q:
        x, y, dist = q.popleft()
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and 0 <= nx < N and 0 <= ny < N:
                if _map[ny][nx] <= size:
                    q.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
                    if 0 < _map[ny][nx] < size:
                        result.append((nx, ny, dist + 1))

    return sorted(result, key=lambda x: (-x[2], -x[1], -x[0]))


ans = 0

while True:
    tmp = bfs(shark[0], shark[1], level)
    if tmp:
        rx, ry, dist = tmp.pop()

        _map[shark[1]][shark[0]], _map[ry][rx] = 0, 0
        shark[0], shark[1] = rx, ry
        ans += dist

        exp += 1
        if exp == level:
            exp = 0
            level += 1
    else:
        break

print(ans)