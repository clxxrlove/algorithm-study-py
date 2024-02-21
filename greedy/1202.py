import sys, heapq

N, K = map(int, sys.stdin.readline().split())
ans = 0

items = []
for _ in range(N):
    heapq.heappush(items, tuple(map(int, sys.stdin.readline().split())))

backs = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
backs.sort()

tmp_items = []
for back in backs:
    while items and back >= items[0][0]:
        heapq.heappush(tmp_items, -heapq.heappop(items)[1])

    if tmp_items:
        ans -= heapq.heappop(tmp_items)
    elif not items:
        break

print(ans)