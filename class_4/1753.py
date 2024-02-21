import sys, heapq

N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().rstrip())
cost = [float("inf") for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]


def dijkstra(start):
    cost[start] = 0
    q = [(0, start)]

    while q:
        dist, node = heapq.heappop(q)

        if cost[node] < dist:
            continue

        for v in graph[node]:
            f_dist = dist + v[1]
            if f_dist < cost[v[0]]:
                cost[v[0]] = f_dist
                heapq.heappush(q, (f_dist, v[0]))


for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K)
for i in range(1, N + 1):
    print(cost[i] if cost[i] != float("inf") else "INF")