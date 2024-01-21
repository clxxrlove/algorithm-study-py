import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]


def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])

    return parent[a]


for _ in range(M):
    command, a, b = map(int, sys.stdin.readline().split())

    a_parent = find_root(a)
    b_parent = find_root(b)

    if command == 0:
        if a > b:
            parent[a_parent] = b_parent
        else:
            parent[b_parent] = a_parent
    else:
        if a_parent != b_parent:
            print("NO")
            continue
        print("YES")