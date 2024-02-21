import sys
from collections import deque

_map = [list(sys.stdin.readline().rstrip()) for _ in range(12)] # 6 * 12 크기의 맵


def bfs(x, y):
    q = deque()
    q.append((x, y))
    s_color = _map[y][x]

    if s_color == '.':
        return False

    visited = set()
    visited.add((x, y))
    result = [(x, y)]

    while q:
        qx, qy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = qx + dx, qy + dy

            if 0 <= nx < 6 and 0 <= ny < 12 and (nx, ny) not in visited:
                if _map[ny][nx] == s_color:
                    result.append((nx, ny))
                    visited.add((nx, ny))
                    q.append((nx, ny))

    return result


def delete(result):
    for rx, ry in result:
        _map[ry][rx] = "."


def down():
    for x in range(6):
        stack = []
        for y in range(12):
            if _map[y][x] != '.':
                stack.append(_map[y][x])
                _map[y][x] = '.'
        if stack:
            for y in range(11, -1, -1):
                if _map[y][x] == '.':
                    if stack and _map[y][x] == '.':
                        _map[y][x] = stack.pop()


def solution():
    ans = 0
    while True:
        flag = 0
        for y in range(12):
            for x in range(6):
                if _map[y][x] != '.':
                    result = bfs(x, y)
                    if len(result) >= 4:
                        flag = 1
                        delete(result)

        if flag == 0:
            break
        down()
        ans += 1
    return ans

print(solution())