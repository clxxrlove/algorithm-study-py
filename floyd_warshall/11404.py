import sys
inf = float("inf")


def floyd_warshall(graph, limit):
    for peek in range(limit):
        for i in range(limit):
            for j in range(limit):
                if i != peek and j != peek and i != j:
                    graph[i][j] = min(graph[i][j], graph[i][peek] + graph[peek][j])


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[inf] * N for _ in range(N)]

for _ in range(M):
    i, j, v = map(int, sys.stdin.readline().split())
    graph[i - 1][j - 1] = min(graph[i - 1][j - 1], v)

floyd_warshall(graph, N)
for g in graph:
    for element in g:
        print(element if element < inf else 0, end=" ")
    print()