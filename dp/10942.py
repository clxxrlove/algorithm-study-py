import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if dp[j + 1][i + j - 1] and arr[j] == arr[i + j]:
            dp[j][i + j] = 1

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a - 1][b - 1])