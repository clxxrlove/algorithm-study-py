import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = set()


def bfs(x, y):
    q = deque([(x, y)])
    visited.add((x, y))
    checked = [(x, y)]
    count = _map[y][x]

    while q:
        qx, qy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = qx + dx, qy + dy

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                diff = abs(_map[qy][qx] - _map[ny][nx])
                if L <= diff <= R:
                    checked.append((nx, ny))
                    count += _map[ny][nx]
                    visited.add((nx, ny))
                    q.append((nx, ny))

    return checked, count


def solution():
    global visited
    day = 0

    while True:
        flag = 0
        visited = set()
        for y in range(N):
            for x in range(N):
                if (x, y) not in visited:
                    result, count = bfs(x, y)
                    if len(result) > 1:
                        flag = 1
                        population = count // len(result)
                        for qx, qy in result:
                            _map[qy][qx] = population

        if flag == 0:
            return day
        else:
            day += 1


print(solution())