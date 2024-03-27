import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
A = list(map(lambda x: -int(x), sys.stdin.readline().split()))
heapq.heapify(A)

B = []
answer = 0

while A or B:
    answer += 1

    while A and len(B) < M:
        heapq.heappush(B, -heapq.heappop(A))

    for i in range(len(B)):
        B[i] -= 1

    while B and B[0] == 0:
        heapq.heappop(B)


print(answer)