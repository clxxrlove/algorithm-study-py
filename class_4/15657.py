# https://www.acmicpc.net/problem/15657
import sys

N, M = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
seq.sort()
result = []


def backtracking(start, depth):
    if depth == M:
        print(*result)
        return

    for i in range(start, N):
        result.append(seq[i])
        backtracking(i, depth + 1)
        result.pop()


backtracking(0, 0)
