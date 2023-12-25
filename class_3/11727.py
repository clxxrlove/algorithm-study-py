# https://www.acmicpc.net/problem/11727
import sys


def dp(x):
    if memo[x] == 0:
        memo[x] = (dp(x - 1) + 2 * dp(x - 2)) % 10007
    return memo[x]


N = int(sys.stdin.readline().rstrip())
memo = [0, 1, 3] + [0] * (N - 2)

print(dp(N))