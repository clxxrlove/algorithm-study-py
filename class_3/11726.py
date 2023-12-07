# https://www.acmicpc.net/problem/11726
import sys

N = int(sys.stdin.readline().rstrip())

memo = [0, 1, 2, 3]

if N >= 4:
    for i in range(4, N + 1):
        memo.append((memo[i - 2] + memo[i - 1]) % 10007)

print(memo[N])