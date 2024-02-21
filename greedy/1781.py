import sys
import heapq

N = int(sys.stdin.readline().rstrip())
ans = 0

problem = []
for _ in range(N):
    d, p = map(int, sys.stdin.readline().split())
    heapq.heappush(problem, (-d, p))

ramen = []
for day in range(-problem[0][0], 0, -1):
    while problem and day <= -problem[0][0]:
        heapq.heappush(ramen, -heapq.heappop(problem)[1])

    if ramen:
        ans -= heapq.heappop(ramen)

print(ans)