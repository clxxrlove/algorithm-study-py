import sys, heapq

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(start, end):
    cost = [float("inf")] * (N + 1)
    cost[start] = 0
    q = [(start, 0)]

    while q:
        _dest, _cost = heapq.heappop(q)

        if cost[_dest] < _cost:
            continue

        for v in graph[_dest]:
            v_cost = _cost + v[1]
            if v_cost < cost[v[0]]:
                cost[v[0]] = v_cost
                heapq.heappush(q, (v[0], v_cost))

    return cost[end]


v1, v2 = map(int, sys.stdin.readline().split())
ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
print(ans if ans < float("inf") else -1)