# https://www.acmicpc.net/problem/15666
import sys

N, M = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
seq.sort()
result = []


def backtracking(start, depth):
    if depth == M:
        print(*result)
        return

    checked = []
    for i in range(start, N):
        if seq[i] not in checked:
            result.append(seq[i])
            checked.append(seq[i])
            backtracking(i, depth + 1)
            result.pop()


backtracking(0, 0)
