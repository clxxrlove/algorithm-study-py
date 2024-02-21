import sys
import heapq

N = int(sys.stdin.readline().rstrip())
ans = 0

assignments = []
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    heapq.heappush(assignments, (-d, w))

scores = []
for day in range(-assignments[0][0], 0, -1):
    while assignments and -assignments[0][0] >= day:
        heapq.heappush(scores, -heapq.heappop(assignments)[1])

    if scores:
        ans -= heapq.heappop(scores)

print(ans)