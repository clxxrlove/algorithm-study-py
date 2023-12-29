# https://www.acmicpc.net/problem/12865
import sys

N, K = map(int, sys.stdin.readline().split())
W = [0] * (N + 1)
V = [0] * (N + 1)
memo = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, sys.stdin.readline().split())
    W[i], V[i] = w, v

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= W[i]:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - W[i]] + V[i])
        else:
            memo[i][j] = memo[i - 1][j]

for m in memo:
    print(*m)
print(memo[N][K])