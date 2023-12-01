# https://www.acmicpc.net/problem/1259
import sys

while True:
    N = sys.stdin.readline().rstrip()
    y = True

    if N[0] == '0':
        break

    for i in range(len(N) // 2):
        if N[i] != N[len(N) - 1 - i]:
            y = False
    print("yes" if y else "no")
