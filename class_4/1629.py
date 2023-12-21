# https://www.acmicpc.net/problem/1629
import sys

A, B, C = map(int, sys.stdin.readline().split())


def multiply(a, n):
    if n == 1:
        return a % C

    if n % 2 == 0:
        return (multiply(a, n // 2) ** 2) % C
    else:
        return ((multiply(a, n // 2) ** 2) * a) % C


result = multiply(A, B)
print(result)