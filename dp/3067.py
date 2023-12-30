# https://www.acmicpc.net/problem/3067
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = [0] + list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    memo = [0] * (M + 1)

    for coin in coins:
        if coin > M:
            continue
        memo[coin] += 1
        for i in range(coin + 1, M + 1):
            memo[i] += memo[i - coin]

    print(memo[M])