# https://www.acmicpc.net/problem/2805
import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)


while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for t in tree:
        if t > mid:
            tmp += t - mid

    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)