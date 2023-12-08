# https://www.acmicpc.net/problem/11651
import sys

N = int(sys.stdin.readline().rstrip())
pos = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pos.append((x, y))

for p in sorted(pos, key=lambda x: (x[1], x[0])):
    print(*p)