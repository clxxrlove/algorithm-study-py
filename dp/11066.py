import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    sum = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        sum[i] = sum[i - 1] + arr[i - 1]

    for i in range(2, N + 1):
        for j in range(1, N - i + 2):
            dp[j][j + i - 1] = (min([dp[j][j + q] + dp[j + q + 1][j + i - 1] for q in range(i - 1)])
                                + sum[j + i - 1] - sum[j - 1])

    print(dp[1][N])
