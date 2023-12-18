# https://www.acmicpc.net/problem/18870
import sys

N = int(sys.stdin.readline().rstrip())
pos = list(map(int, sys.stdin.readline().split()))
newPos = sorted(list(set(pos)))
result = {v: i for i, v in enumerate(newPos)}

for p in pos:
    print(result[p], end=" ")