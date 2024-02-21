import sys

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(line) - 2, 2):
        graph[line[0]].append([line[i], line[i + 1]])
        graph[line[i]].append([line[0], line[i + 1]])


def dfs(start, dist):
    for v in graph[start]:
        if visited[v[0]] == -1:
            visited[v[0]] = v[1] + dist
            dfs(v[0], visited[v[0]])


dfs(1, 0)
result = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[result] = 0
dfs(result, 0)

print(max(visited))