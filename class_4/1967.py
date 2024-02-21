import sys

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
visited[1] = 0

for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])


def dfs(start, _dist):
    for v in graph[start]:
        node, dist = v
        if visited[node] == -1:
            visited[node] = _dist + dist
            dfs(node, visited[node])


dfs(1, 0)
tmp = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[tmp] = 0

dfs(tmp, 0)
print(max(visited))