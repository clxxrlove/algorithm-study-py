import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

parent = [i for i in range(N + 1)]


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]


def union(_a, _b):
    a = find(_a)
    b = find(_b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def check(a, b):
    if find(a) == find(b):
        return True
    return False


for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for t in range(len(tmp)):
        if tmp[t] == 1:
            union(i + 1, t + 1)


plan = list(map(int, sys.stdin.readline().split()))
ans = 1

for p in range(1, len(plan)):
    if not check(plan[p], plan[p - 1]):
        ans = 0
        break

print("YES" if ans == 1 else "NO")