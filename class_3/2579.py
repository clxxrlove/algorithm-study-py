# https://www.acmicpc.net/problem/2579
import sys

N = int(sys.stdin.readline().rstrip())
stairs = [0]
memo = [[0] * (N + 1) for _ in range(2)]

for _ in range(N):
    stairs.append(int(sys.stdin.readline().rstrip()))

memo[0][1], memo[1][1] = stairs[1], stairs[1]

for n in range(2, N + 1):
    memo[0][n] = memo[1][n - 1] + stairs[n]
    memo[1][n] = max(memo[1][n - 2], memo[0][n - 2]) + stairs[n]

print(max(memo[1][N], memo[0][N]))