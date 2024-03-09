import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
dp = [-1] * (N + 1)

for i, item in enumerate(arr):
    dp[item] = i

longest, count = 0, 1

for i in range(1, N):
    if dp[i] < dp[i + 1]:
        count += 1
    else:
        longest = max(longest, count)
        count = 1

print(N - longest if N > 1 else 0)