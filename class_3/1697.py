# https://www.acmicpc.net/problem/1697
import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

N, K = map(int, sys.stdin.readline().split())
t = float("inf")
visited = [False] * 100001

def bfs(N, visited):
    global t, K
    queue = deque([[N, 0]])
    visited[N] = True
    while queue:
        q = queue.popleft()
        x, time = q[0], q[1]
        if x == K:
            t = min(t, time)

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                queue.append([i, time + 1])


bfs(N, visited)
print(t)