# https://www.acmicpc.net/problem/9095
import sys

N = int(sys.stdin.readline().rstrip())
case = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

memo = [0, 1, 2, 4]

if max(case) >= 4:
    for i in range(4, max(case) + 1):
        memo.append(memo[i - 3] + memo[i - 2] + memo[i - 1])

for c in case:
    print(memo[c])