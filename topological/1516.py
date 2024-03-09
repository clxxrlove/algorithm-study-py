import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
t = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    commands = list(map(int, sys.stdin.readline().split()))
    t[i] = commands[0]

    for command in commands[1:-1]:
        graph[command].append(i)
        in_degree[i] += 1

queue = deque()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)
        dp[i] = t[i]

while queue:
    q = queue.popleft()

    for v in graph[q]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)
        dp[v] = max(dp[q] + t[v], dp[v])

for d in dp[1:]:
    print(d)