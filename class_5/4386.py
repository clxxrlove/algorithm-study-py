import sys
from math import sqrt


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


N = int(sys.stdin.readline().rstrip())
star = [tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]
edges = []

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        line = sqrt(abs(star[i][0] - star[j][0]) ** 2 + abs(star[i][1] - star[j][1]) ** 2)
        edges.append((line, i, j))

edges.sort()

parent = [i for i in range(N)]

answer = 0
for cost, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        answer += cost

print(f"%.2f" % answer)