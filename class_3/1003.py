# https://www.acmicpc.net/problem/1003
import sys

N = int(sys.stdin.readline().rstrip())
case = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

one = [0, 1, 1]
zero = [1, 0, 1]

if max(case) >= 3:
    for i in range(3, max(case) + 1):
        one.append(one[i - 1] + one[i - 2])
        zero.append(zero[i - 1] + zero[i - 2])

for c in case:
    print(zero[c], one[c])