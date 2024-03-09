import sys
from bisect import bisect_left, bisect_right

T = int(sys.stdin.readline().rstrip())

An = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

Bn = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))

As, Bs = [], []

for i in range(An):
    tmp = A[i]
    As.append(tmp)
    for j in range(i + 1, An):
        tmp += A[j]
        As.append(tmp)

for i in range(Bn):
    tmp = B[i]
    Bs.append(tmp)
    for j in range(i + 1, Bn):
        tmp += B[j]
        Bs.append(tmp)

As.sort()
Bs.sort()

answer = 0
for i in range(len(As)):
    answer += bisect_right(Bs, T - As[i]) - bisect_left(Bs, T - As[i])

print(answer)