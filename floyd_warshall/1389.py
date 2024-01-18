import sys
inf = float("inf")


def floyd_warshall(graph, limit):
    for peek in range(limit):
        for i in range(limit):
            for j in range(limit):
                if i != peek and j != peek and i != j:
                    graph[i][j] = min(graph[i][j], graph[i][peek] + graph[peek][j])


N, M = map(int, sys.stdin.readline().split())
graph = [[inf] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

floyd_warshall(graph, N)
ans = [inf]

for g in graph:
    ans.append(sum(g))

print(ans.index(min(ans)))