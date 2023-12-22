# https://www.acmicpc.net/problem/11660
import sys

N, M = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        memo[i][j] = memo[i][j - 1] + memo[i - 1][j] - memo[i - 1][j - 1] + table[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = memo[x2][y2] - memo[x1 - 1][y2] - memo[x2][y1 - 1] + memo[x1 -1][y1 - 1]
    print(result)