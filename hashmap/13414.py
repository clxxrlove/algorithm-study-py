# https://www.acmicpc.net/problem/13414
import sys

N, M = map(int, sys.stdin.readline().split())
s = dict()
count = 0

for i in range(M):
    stu_code = sys.stdin.readline().rstrip()
    s[stu_code] = i

for i in sorted(s.items(), key=lambda x: x[1]):
    if count >= N:
        break
    count += 1
    print(i[0])
