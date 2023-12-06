# https://www.acmicpc.net/problem/11659
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
accum = [0, nums[0]]

for i in range(1, len(nums)):
    accum.append(accum[i] + nums[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(accum[j] - accum[i - 1])
