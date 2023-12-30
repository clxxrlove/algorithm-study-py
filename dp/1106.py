# https://www.acmicpc.net/problem/1106
import sys
inf = float("inf")

C, N = map(int, sys.stdin.readline().split())
countries = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    countries.append((W, V))

memo = [0] + [inf] * (C + 100)

for w, v in countries:
    for i in range(1, C + 101):
        if i >= v:
            memo[i] = min(memo[i], memo[i - v] + w)

ans = memo[C]

for i in range(C, C + 101):
    ans = min(ans, memo[i])

print(ans)