import sys
from collections import deque


def solution():
    global cheese
    answer = 0

    while True:
        dead_cheese = bfs()

        if cheese == len(dead_cheese):
            return answer + 1, len(dead_cheese)

        for dx, dy in dead_cheese:
            board[dy][dx] = 0

        cheese -= len(dead_cheese)
        answer += 1


def bfs():
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))

    c = set()

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited:
                if board[ny][nx] == 1:
                    board[ny][nx] = 2 # 곧 녹을 치즈임
                    c.add((nx, ny))
                    continue
                elif board[ny][nx] == 0:
                    q.append((nx, ny))
                    visited.add((nx, ny))

    return list(c)


N, M = map(int, sys.stdin.readline().split()) # y, x
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cheese = 0

for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            cheese += 1

time, count = solution()

print(time)
print(count)