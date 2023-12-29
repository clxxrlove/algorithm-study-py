# https://www.acmicpc.net/problem/9019
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())


def bfs(start, end):
    queue = deque([[start, ""]])
    visited = [False] * 10000
    command = {0: "D", 1: "S", 2: "L", 3: "R"}

    while queue:
        q, ans = queue.popleft()
        commands = [q * 2 % 10000, (q - 1) % 10000, q // 1000 + (q % 1000) * 10, q // 10 + (q % 10) * 1000]

        if q == end:
            return ans

        for i in range(4):
            if not visited[commands[i]]:
                visited[commands[i]] = True
                queue.append([commands[i], ans + command[i]])


for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    ans = bfs(start, end)
    print(ans)