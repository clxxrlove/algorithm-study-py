import sys

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 0: 대각, 1: 가로, 2: 세로

dp[1][0][1] = 1

for i in range(2, N):
    if graph[0][i] == 0:
        dp[1][0][i] = dp[1][0][i - 1]

for i in range(1, N): # y
    for j in range(1, N): # x
        # 대각선 계산
        if graph[i][j - 1] == 0 and graph[i - 1][j] == 0 and graph[i][j] == 0:
            dp[0][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        # 가로, 세로 계산
        if graph[i][j] == 0:
            dp[1][i][j] = dp[1][i][j - 1] + dp[0][i][j - 1]
            dp[2][i][j] = dp[2][i - 1][j] + dp[0][i - 1][j]

ans = 0
for i in range(3):
    ans += dp[i][N - 1][N - 1]

print(ans)