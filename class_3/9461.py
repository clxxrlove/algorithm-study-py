# https://www.acmicpc.net/problem/9461
import sys


def dp(x):
    if x < 5:
        return memo[x]
    if memo[x] == 0:
        memo[x] = dp(x - 1) + dp(x - 5)
    return memo[x]


T = int(sys.stdin.readline().rstrip())
memo = [0, 1, 1, 1, 2] + [0] * 96

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(dp(N))
