import sys

N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(N + 1)]

if N % 2 == 1:
    print(0)
else:
    dp[2] = 3
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(2, i - 2, 2):
            dp[i] += dp[j] * 2

    print(dp[N])