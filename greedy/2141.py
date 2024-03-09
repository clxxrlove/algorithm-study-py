import sys

N = int(sys.stdin.readline().rstrip())

_sum = 0
office = []
for i in range(N):
    a, x = map(int, sys.stdin.readline().split())
    office.append([a, x])
    _sum += x

office.sort(key=lambda x: x[0])

cur = 0
for i in range(N):
    cur += office[i][1]
    if cur >= _sum / 2:
        print(office[i][0])
        break