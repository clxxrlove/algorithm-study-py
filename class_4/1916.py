# https://www.acmicpc.net/problem/1916
import sys, heapq
MAX = float("inf")

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

cost = [MAX] * (N + 1)
graph = [[] for _ in range(N + 1)]


def dijkstra(start):
    q = [(start, 0)]
    cost[start] = 0

    while q:
        dest, dest_cost = heapq.heappop(q)

        if dest_cost > cost[dest]:
            continue

        for i in graph[dest]:
            f_cost = dest_cost + i[1]
            if f_cost < cost[i[0]]:
                cost[i[0]] = f_cost
                heapq.heappush(q, (i[0], f_cost))


for i in range(M):
    start, end, bus_cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, bus_cost))

a_start, a_end = map(int, sys.stdin.readline().split())

dijkstra(a_start)
print(cost[a_end])

