# https://www.acmicpc.net/problem/14728
import sys

N, T = map(int, sys.stdin.readline().split())
study = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [0] * (T + 1)

for w, v in study:
    for i in range(T, -1, -1):
        if i >= w:
            memo[i] = max(memo[i], memo[i - w] + v)

print(memo[T])