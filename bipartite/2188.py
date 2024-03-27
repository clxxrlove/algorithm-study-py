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


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for i in range(N):
    cow = list(map(int, sys.stdin.readline().split()))

    for c in cow[1:]:
        graph[i].append(c)

selected = [-1] * (M + 1)
answer = 0

for i in range(N):
    visited = [False] * (N + 1)
    if dfs(i):
        answer += 1

print(answer)