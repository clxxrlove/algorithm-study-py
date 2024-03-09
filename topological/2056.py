import sys
from collections import deque


def topological_sort(n):
    global answer
    queue = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        q = queue.popleft()
        for v in graph[q]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
            dp[v] = max(dp[q] + time[v], dp[v])


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]

in_degree = [0] * (N + 1)
time = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    task = list(map(int, sys.stdin.readline().split()))
    time[i] = task[0]

    for t in range(task[1]):
        graph[task[2 + t]].append(i)
        in_degree[i] += 1

topological_sort(N)
print(max(dp))