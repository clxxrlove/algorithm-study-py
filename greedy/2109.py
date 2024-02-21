import sys
import heapq

N = int(sys.stdin.readline().rstrip())

if N == 0:
    print(0)
    exit()

ans = 0
lecture = []

for _ in range(N):
    p, d = map(int, sys.stdin.readline().split())
    heapq.heappush(lecture, (-d, p))

pay = []
for day in range(-lecture[0][0], 0, -1):
    while lecture and day <= -lecture[0][0]:
        heapq.heappush(pay, -heapq.heappop(lecture)[1])

    if pay:
        ans -= heapq.heappop(pay)

print(ans)