# https://www.acmicpc.net/problem/1259
import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().split()))
num = [i for i in range(2, max(M) + 1)]
acc = 0

for n in num:
    if n == 0: continue
    for k in range(n * 2, len(num) + 2, n):
        num[k - 2] = 0

for m in M:
    if m in num:
        acc += 1

print(acc)