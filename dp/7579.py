# https://www.acmicpc.net/problem/7579
import sys

N, M = map(int, sys.stdin.readline().split())
W = list(map(int, sys.stdin.readline().split()))
V = list(map(int, sys.stdin.readline().split()))
sumCost = sum(V) + 1
memo = [[0] * (sumCost + 100) for _ in range(N + 1)]

ans = int(1e9)

for i in range(N):
    memory, cost = W[i], V[i]
    for j in range(sumCost + 99, -1, -1):
        if j >= cost:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - cost] + memory)
            if memo[i][j] >= M:
                ans = min(ans, j)
        else:
            memo[i][j] = memo[i - 1][j]

print(ans)