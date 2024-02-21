import sys, heapq

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
cost = [float("inf")] * (N + 1)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


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


dijkstra(X)
dest_cost = cost.copy()
ans = 0

for i in range(1, N + 1):
    cost = [float("inf")] * (N + 1)
    dijkstra(i)
    ans = max(ans, dest_cost[i] + cost[X])

print(ans)