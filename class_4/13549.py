# https://www.acmicpc.net/problem/13549
import sys, heapq
INF = float("inf")

N, K = map(int, sys.stdin.readline().split())


def dijkstra(start):
    q = [(start, 0)]
    time[start] = 0

    while q:
        dist, d_time = heapq.heappop(q)

        if d_time > time[dist]:
            continue

        for i in graph[dist]:
            f_time = d_time + i[1]
            if f_time < time[i[0]]:
                time[i[0]] = f_time
                heapq.heappush(q, (i[0], f_time))


time = [INF] * ((K + 1) * 2 + 1)
graph = [[] for _ in range((K + 1) * 2 + 1)]

for i in range(0, K + 2):
    graph[i].append((i - 1, 1))
    graph[i].append((i + 1, 1))
    graph[i].append((i * 2, 0))

if N > K:
    print(N - K)
    exit(0)

dijkstra(N)
print(time[K])