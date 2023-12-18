# https://www.acmicpc.net/problem/15654
import sys

N, M = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
seq.sort()
result = []


def backtracking():
    if len(result) == M:
        print(*result)
        return

    for i in seq:
        if i not in result:
            result.append(i)
            backtracking()
            result.pop()


backtracking()