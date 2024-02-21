import sys, heapq

N = int(sys.stdin.readline().rstrip())
A = []
ans = 0

if N == 1:
    print(0)
    exit()

for _ in range(N):
    heapq.heappush(A, int(sys.stdin.readline().rstrip()))

for _ in range(N - 1):
    first = heapq.heappop(A)
    second = heapq.heappop(A)
    heapq.heappush(A, first + second)
    ans += first + second

print(ans)