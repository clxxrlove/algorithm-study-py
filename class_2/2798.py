# https://www.acmicpc.net/problem/11050
import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
card = 0

for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            card = max(card, num[i] + num[j] + num[k]) if num[i] + num[j] + num[k] <= M else card

print(card)