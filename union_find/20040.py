import sys

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N)]


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]


def union(a, b):
    a_root, b_root = find(a), find(b)

    if a_root > b_root:
        parent[a_root] = b_root
    else:
        parent[b_root] = a_root


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(i + 1)
        exit(0)
    union(a, b)

print(0)