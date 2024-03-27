import sys
from collections import deque
from copy import copy


def deepcopy(iterator):
    return [item[:] for item in iterator]


def bfs(x, y):
    q = deque()
    visited = set()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] > 0 and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))

    return visited


def simulation(_set: set):
    deleted = set()
    copied = deepcopy(graph)

    for sx, sy in _set:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = sx + dx, sy + dy

            if 0 <= nx < M and 0 <= ny < N:
                if copied[ny][nx] == 0:
                    if graph[sy][sx] == 0:
                        continue
                    graph[sy][sx] -= 1

        if graph[sy][sx] == 0:
            deleted.add((sx, sy))
            first.remove((sx, sy))

    return deleted


def check(res_set: set, diff_set: set):
    if len(res_set) != len(diff_set):
        return False
    return True


N, M = map(int, sys.stdin.readline().split()) # y, x
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
first = set()

xx, yy = -1, -1
zero = False

for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            first.add((j, i))
            xx, yy = j, i
        else:
            zero = True

if not zero:
    print(0)
    exit()

diff = bfs(xx, yy)

while True:
    if not check(first, diff):
        break

    deleted = simulation(diff)

    if len(deleted) == len(diff):
        if len(first) == 0:
            answer = 0
        break

    diff = diff.difference(deleted)
    first = first.difference(deleted)

    xx, yy = diff.pop()
    diff.add((xx, yy))

    diff = bfs(xx, yy)
    answer += 1

print(answer)