import sys
from collections import deque


def topological_sort(v):
    result = []
    queue = deque()

    for i in range(1, v + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        q = queue.popleft()
        result.append(q)
        for i in graph[q]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    print(*result)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    in_degree[b] += 1

topological_sort(N)