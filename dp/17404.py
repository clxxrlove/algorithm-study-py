import sys

N = int(sys.stdin.readline().rstrip())
color = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N))
ans = float("inf")

for i in range(3):
    dp = [[float("inf")] * 3 for _ in range(N)]
    dp[0][i] = color[0][i]

    for j in range(1, N):
        dp[j][0] = color[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = color[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = color[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for k in range(3):
        if i == k:
            continue
        ans = min(ans, dp[N - 1][k])


print(ans)