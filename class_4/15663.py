# https://www.acmicpc.net/problem/15663
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
visited = [False] * (N + 1)
seq = []
result = []


def backtracking(tmp):
    if len(seq) == M:
        result.append(tuple(seq))
        return

    for i in range(0, len(nums)):
        if not visited[i] and tmp != i:
            visited[i] = True
            seq.append(nums[i])
            tmp = i
            backtracking(tmp)
            visited[i] = False
            seq.pop()


backtracking(-1)
result = sorted(list(set(result)))
for r in result:
    print(*r)