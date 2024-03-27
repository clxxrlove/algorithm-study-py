import sys
import heapq

N = int(sys.stdin.readline().rstrip())
rest = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split()) # 거리, 기름양
    rest.append((a, b))

rest.sort(key=lambda x: (x[0], -x[1]))

L, fuel = map(int, sys.stdin.readline().split())
rest.append((L, 0))

tmp = []
current = 0
answer = 0
for dist, oil in rest:
    if fuel >= L:
        break

    while tmp and fuel < dist:
        fuel += -heapq.heappop(tmp)
        answer += 1

    if fuel < dist:
        break

    heapq.heappush(tmp, -oil)

print(answer if fuel >= L else -1)