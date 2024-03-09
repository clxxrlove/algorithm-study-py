import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    sequence = list(map(int, sys.stdin.readline().split()))

    for i in range(1, sequence[0]):
        graph[sequence[i]].append(sequence[i + 1])
        in_degree[sequence[i + 1]] += 1

queue = deque()
result = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    q = queue.popleft()
    result.append(q)

    for v in graph[q]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)