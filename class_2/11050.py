# https://www.acmicpc.net/problem/11050
import sys


def factorial(a):
    if a == 0 or a == 1:
        return 1
    return a * factorial(a - 1)


N, K = map(int, sys.stdin.readline().split())
print(factorial(N) // (factorial(K) * factorial(N - K)))