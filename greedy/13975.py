import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    file = list(map(int, sys.stdin.readline().split()))
    answer = 0

    heapq.heapify(file)

    while file:
        if len(file) == 1:
            break

        first = heapq.heappop(file)
        second = heapq.heappop(file)

        answer += first + second
        heapq.heappush(file, first + second)

    print(answer)