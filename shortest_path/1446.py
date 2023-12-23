# https://www.acmicpc.net/problem/1446
import sys, heapq


def dijkstra(graph, start):
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, vert = heapq.heappop(q)

        if dist > distance[vert]:
            continue

        for i in graph[vert]:
            f_dist = dist + i[1]
            if f_dist < distance[i[0]]:
                distance[i[0]] = f_dist
                heapq.heappush(q, (f_dist, i[0]))


N, D = map(int, sys.stdin.readline().split())
path = [[] for _ in range(D + 1)]
distance = [float("inf")] * (D + 1)

for i in range(D):
    path[i].append((i + 1, 1))

for _ in range(N):
    start, end, dist = map(int, sys.stdin.readline().split())
    if start > end or end > D:
        continue
    path[start].append((end, dist))


dijkstra(path, 0)
print(distance[D])