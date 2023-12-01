# https://www.acmicpc.net/problem/2609
import sys


def Euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, M = map(int, sys.stdin.readline().split())
e = Euclidean(N, M)

print(e)
print(N * M // e)