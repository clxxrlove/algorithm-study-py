# https://www.acmicpc.net/problem/11053
import sys

N = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().split()))
memo = [1] * N

for i in range(1, N):
    for j in range(i):
        if seq[i] > seq[j]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))