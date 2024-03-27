import sys


def dfs(n):
    if visited[n]:
        return False
    visited[n] = True

    for v in graph[n]:
        if selected[v] == -1 or dfs(selected[v]):
            selected[v] = n
            return True

    return False


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(M)]
    selected = [-1] * (N + 1)

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        for n in range(a, b + 1):
            graph[i].append(n)

    for i in range(M):
        visited = [False for _ in range(M)]
        dfs(i)

    print(len(selected) - selected.count(-1))