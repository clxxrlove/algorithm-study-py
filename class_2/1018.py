# https://www.acmicpc.net/problem/1018
import sys

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(N)]
start = ["B", "W"]
square = []

for i in range(M - 7):
    for j in range(N - 7):
        before = ""
        for s in start:
            acc = 0
            before = s
            for m in range(i, 8 + i):
                if before == "B":
                    before = "W"
                else:
                    before = "B"
                for n in range(j, 8 + j):
                    if board[n][m] == before:
                        if before == "B":
                            before = "W"
                        else:
                            before = "B"
                        acc += 1
                    else:
                        before = board[n][m]

            square.append(acc)

print(min(square))

