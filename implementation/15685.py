import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(sys.stdin.readline().rstrip())
board = [[0] * 101 for _ in range(101)]
answer = 0

for _ in range(N):
    y, x, d, g = map(int, sys.stdin.readline().split())  # d는 시작 방향, g는 세대 수
    board[y][x] = 1
    curve = [d]

    for _ in range(g):
        for c in range(len(curve) - 1, -1, -1):
            curve.append((curve[c] + 1) % 4)

    for c in range(len(curve)):
        x, y = x + dx[curve[c]], y + dy[curve[c]]
        board[y][x] = 1

for x in range(100):
    for y in range(100):
        if board[y][x] == 1 and board[y + 1][x] == 1 and board[y][x + 1] == 1 and board[y + 1][x + 1] == 1:
            answer += 1

print(answer)