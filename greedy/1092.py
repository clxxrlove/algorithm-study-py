import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)

M = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort(reverse=True)

ans = 0

if boxes[0] > cranes[0]:
    print(-1)
    exit()

while boxes:
    for crane in cranes:
        if boxes and crane < boxes[-1]:
            continue
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    ans += 1

print(ans)