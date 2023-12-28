# https://www.acmicpc.net/problem/7662
import sys, heapq
from collections import Counter

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    nums = Counter()
    minHeap = []
    maxHeap = []

    for _ in range(K):
        case = sys.stdin.readline().split()
        command, num = case[0], int(case[1])

        if command == "I":
            nums[num] += 1
            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, num)
        elif command == "D":
            if any(nums.values()):
                if num == 1:
                    while -maxHeap[0] not in nums or nums[-maxHeap[0]] == 0:
                        tmp = -heapq.heappop(maxHeap)
                        if tmp in nums:
                            del (nums[tmp])
                    nums[-maxHeap[0]] -= 1
                else:
                    while minHeap[0] not in nums or nums[minHeap[0]] == 0:
                        tmp = heapq.heappop(minHeap)
                        if tmp in nums:
                            del (nums[tmp])
                    nums[minHeap[0]] -= 1

    if any(nums.values()):
        while -maxHeap[0] not in nums or nums[-maxHeap[0]] == 0:
            heapq.heappop(maxHeap)
        while minHeap[0] not in nums or nums[minHeap[0]] == 0:
            heapq.heappop(minHeap)
        print(-maxHeap[0], minHeap[0])
    else:
        print("EMPTY")
