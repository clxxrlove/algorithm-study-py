import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = True
    count = 1

    for i in graph[v]:
        if not visited[i]:
            count += dfs(graph, i, visited)

    return count


ans = dfs(graph, 1, visited)
print(ans - 1)