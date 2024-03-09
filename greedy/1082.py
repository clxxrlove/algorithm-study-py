import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
dp = [-1] * (M + 1)

for i in range(N - 1, -1, -1):
    tmp = P[i]
    for j in range(tmp, M + 1):
        dp[j] = max(dp[j], i, dp[j - tmp] * 10 + i)

print(dp[M])