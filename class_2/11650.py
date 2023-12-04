# https://www.acmicpc.net/problem/11650
import sys

N = int(sys.stdin.readline().rstrip())
pos = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pos.append((x, y))

for p in sorted(pos, key=lambda x: (x[0], x[1])):
    print(*p)