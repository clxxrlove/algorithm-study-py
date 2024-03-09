import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, sys.stdin.readline().split())
parent = list(range(V + 1))
graph = []

for _ in range(E):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph.append((cost, x, y))

graph.sort()

answer = 0
for cost, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)
