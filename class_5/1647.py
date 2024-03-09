import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    x, y = find(x), find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, sys.stdin.readline().split())
parent = list(range(N + 1))
edge = []

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    edge.append((cost, a, b))

edge.sort()

answer = 0
last = 0
for cost, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        answer += cost
        last = cost

print(answer - last)