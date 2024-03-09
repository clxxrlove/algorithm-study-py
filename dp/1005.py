import sys
from collections import deque


def topological_sort(v):
    ans = 0
    queue = deque()

    for i in range(1, v + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = d[i]

    while queue:
        q = queue.popleft()

        for i in graph[q]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[q] + d[i])
            if in_degree[i] == 0:
                queue.append(i)


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    d = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(N + 1)]

    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    target = int(sys.stdin.readline().rstrip())

    topological_sort(N)
    print(dp[target])