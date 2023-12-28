# https://www.acmicpc.net/problem/1654
import sys

N, M = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for l in lan:
        if l >= mid:
            lines += l // mid

    if lines >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)