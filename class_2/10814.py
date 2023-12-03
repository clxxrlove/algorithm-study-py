# https://www.acmicpc.net/problem/10814
import sys

N = int(sys.stdin.readline().rstrip())
user = list()

for _ in range(N):
    A, B = sys.stdin.readline().split()
    user.append([int(A), B])

for u in sorted(user, key=lambda x:x[0]):
    print(u[0], u[1])