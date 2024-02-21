import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
queue = deque(map(int, sys.stdin.readline().split()))
multitap = set()
ans = 0

while queue:
    q_next = queue.popleft()
    if q_next in multitap:
        continue
    q_difference = multitap.difference(set(queue))

    if len(multitap) == N:
        if q_difference:
            for tap in list(multitap):
                if tap in q_difference:
                    ans += 1
                    multitap.remove(tap)
                    break
        else:
            index = -1
            for tap in multitap:
                index = max(index, queue.index(tap))
            multitap.remove(queue[index])
            ans += 1

    multitap.add(q_next)

print(ans)