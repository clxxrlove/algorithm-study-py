# https://www.acmicpc.net/problem/1149
import sys

N = int(sys.stdin.readline().rstrip())
colors = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[0] * 3 for _ in range(N)]
memo[0] = colors[0]

for i in range(1, N):
    if memo[i][0] == 0:
        memo[i][0] = min(memo[i - 1][1], memo[i - 1][2]) + colors[i][0]
    if memo[i][1] == 0:
        memo[i][1] = min(memo[i - 1][0], memo[i - 1][2]) + colors[i][1]
    if memo[i][2] == 0:
        memo[i][2] = min(memo[i - 1][0], memo[i - 1][1]) + colors[i][2]

print(min(memo[N - 1]))