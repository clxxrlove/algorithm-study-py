# https://www.acmicpc.net/problem/16953
import sys
from collections import deque


def bfs(start, target):
    queue = deque([(start, 1)])

    while queue:
        v, depth = queue.popleft()
        procedure = [v * 2, v * 10 + 1]

        for p in procedure:
            if p == target:
                return depth + 1
            if p < target:
                queue.append((p, depth + 1))


N, M = map(int, sys.stdin.readline().split())
result = bfs(N, M)

print(result if result else -1)