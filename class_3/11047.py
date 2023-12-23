# https://www.acmicpc.net/problem/11047
import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
result = 0

for coin in reversed(coins):
    result += K // coin
    K %= coin

print(result)