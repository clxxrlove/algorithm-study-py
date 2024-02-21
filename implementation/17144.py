import sys
import copy
from collections import deque

R, C, T = map(int, sys.stdin.readline().split()) # y, x
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cleaner = []

for y in range(R):
    for x in range(C):
        if _map[y][x] == -1:
            cleaner.append((x, y))


def check(x, y):
    result = []
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < C and 0 <= ny < R:
            if _map[ny][nx] == -1:
                continue
            result.append((nx, ny))

    return result


def find_dust():
    result = []

    for y in range(R):
        for x in range(C):
            if _map[y][x] > 0:
                result.append((x, y))

    return result


def diffusion():
    global _map
    dusts = find_dust()
    new_map = copy.deepcopy(_map)

    for dust in dusts:
        checked = check(dust[0], dust[1])

        if checked:
            counter = _map[dust[1]][dust[0]] // 5
            for nx, ny in checked:
                new_map[ny][nx] += counter
            new_map[dust[1]][dust[0]] -= counter * len(checked)

    _map = new_map


def clean(x, y, direction):
    queue = deque()
    cursor_x, cursor_y = x + 1, y
    d = 0

    while True:
        tmp = 0
        if x == cursor_x and y == cursor_y:
            break

        if queue:
            tmp = queue.popleft()

        queue.append(_map[cursor_y][cursor_x])
        _map[cursor_y][cursor_x] = tmp if tmp > 0 else 0

        dx, dy = cursor_x + direction[d][0], cursor_y + direction[d][1]

        if dx < 0 or dx >= C or dy < 0 or dy >= R:
            d += 1

        cursor_x, cursor_y = cursor_x + direction[d][0], cursor_y + direction[d][1]


def _upper_clean():
    clean(cleaner[0][0], cleaner[0][1], [(1, 0), (0, -1), (-1, 0), (0, 1)])


def _lower_clean():
    clean(cleaner[1][0], cleaner[1][1], [(1, 0), (0, 1), (-1, 0), (0, -1)])


for _ in range(T):
    diffusion()
    _upper_clean()
    _lower_clean()

ans = 0
for m in _map:
    ans += sum(m)

print(ans + 2)