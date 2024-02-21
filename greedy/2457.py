import sys
import heapq

N = int(sys.stdin.readline().rstrip())
start, end = (3, 1), (11, 30)
ans = 0

flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, sys.stdin.readline().split())
    heapq.heappush(flowers, [(sm, sd), (-em, -ed)])

ends = []

while flowers:
    if flowers[0][0] > start:
        break
        
    while flowers and flowers[0][0] <= start:
        heapq.heappush(ends, heapq.heappop(flowers)[1])

    if ends:
        ans += 1
        end_day = heapq.heappop(ends)
        start = (-end_day[0], -end_day[1])
        if start > end:
            break

        ends.clear()

print(0 if start <= end else ans)