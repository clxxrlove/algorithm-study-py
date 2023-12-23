# https://www.acmicpc.net/problem/9465
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    memo = [[0] * N for _ in range(2)]

    for i in range(N):
        if i >= 2:
            memo[0][i] = max(memo[1][i - 1], memo[1][i - 2]) + stickers[0][i]
            memo[1][i] = max(memo[0][i - 1], memo[0][i - 2]) + stickers[1][i]
        elif i == 1:
            memo[0][i] = memo[1][i - 1] + stickers[0][i]
            memo[1][i] = memo[0][i - 1] + stickers[1][i]
        else:
            memo[0][i] = stickers[0][i]
            memo[1][i] = stickers[1][i]

    print(max(memo[0][N - 1], memo[1][N - 1]))