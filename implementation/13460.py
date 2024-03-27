import sys
from collections import deque


def bfs(r1, r2, b1, b2):
    q = deque()
    q.append((r1, r2, b1, b2, 0))

    visited = set()
    visited.add((r1, r2, b1, b2))

    while q:
        rx, ry, bx, by, count = q.popleft()

        if count >= 10:
            return -1

        if board[ry][rx] == "O":
            return count

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rnx, rny = rx, ry
            while True:
                rnx += dx
                rny += dy

                if board[rny][rnx] == "#":
                    rnx -= dx
                    rny -= dy
                    break

                if board[rny][rnx] == "O":
                    break

            bnx, bny = bx, by
            while True:
                bnx += dx
                bny += dy

                if board[bny][bnx] == "#":
                    bnx -= dx
                    bny -= dy
                    break

                if board[bny][bnx] == "O":
                    break

            if board[bny][bnx] != "O":
                if board[rny][rnx] == "O":
                    return count + 1

                if rnx == bnx and rny == bny:
                    if abs(bnx - bx) + abs(bny - by) < abs(rnx - rx) + abs(rny - ry):
                        rnx -= dx
                        rny -= dy
                    else:
                        bnx -= dx
                        bny -= dy

                if (rnx, rny, bnx, bny) not in visited:
                    q.append((rnx, rny, bnx, bny, count + 1))
                    visited.add((rnx, rny, bnx, bny))

    return -1


N, M = map(int, sys.stdin.readline().split()) # y, x -> N == x, M == y
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

redx, redy = -1, -1
bluex, bluey = -1, -1

for i in range(N): # y
    for j in range(M): # x
        if board[i][j] == "R":
            redx, redy = j, i
        elif board[i][j] == "B":
            bluex, bluey = j, i

answer = bfs(redx, redy, bluex, bluey)

print(answer)