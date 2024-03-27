import sys
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))

    c = set()
    d = set()

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if board[ny][nx] == 0:
                    if (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                    continue
                elif board[ny][nx] == 1:
                    board[ny][nx] = 2
                    d.add((nx, ny))
                elif board[ny][nx] == 2:
                    c.add((nx, ny))

    for dx, dy in d.difference(c):
        board[dy][dx] = 1

    return list(c)


def solution():
    global cheese
    answer = 0

    while True:
        dead_cheese = bfs()

        if cheese == len(dead_cheese):
            return answer + 1

        for dx, dy in dead_cheese:
            board[dy][dx] = 0

        cheese -= len(dead_cheese)

        answer += 1


N, M = map(int, sys.stdin.readline().split()) # y, x
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cheese = 0

for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            cheese += 1

answer = solution()
print(answer)