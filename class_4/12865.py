# https://www.acmicpc.net/problem/12865
import sys
INF = float("inf")

N, K = map(int, sys.stdin.readline().split())
C = [0] + list(map(int, sys.stdin.readline().split()))
memo = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, K + 1):
    memo[0][i] = INF

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= C[i]:
            memo[i][j] = min(memo[i - 1][j], memo[i - 1][j - C[i]] + 1)
        else:
            memo[i][j] = memo[i - 1][j]

print(-1 if memo[N][K] == INF else memo[N][K])