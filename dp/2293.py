# https://www.acmicpc.net/problem/2293
import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
d = [0] * (K + 1)
d[0] = 1

for c in coins:
    for i in range(c, K + 1):
        d[i] = d[i] + d[i - c]

print(d[K])