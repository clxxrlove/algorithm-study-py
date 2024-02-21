import sys
import heapq

N = int(sys.stdin.readline().strip())
classes = []

for _ in range(N):
    classes.append(tuple(map(int, sys.stdin.readline().split())))
classes.sort(key=lambda x: (x[0], x[1]))

tmp_classes = [classes[0][1]]
for i in range(1, N):
    if tmp_classes[0] <= classes[i][0]:
        heapq.heappop(tmp_classes)
    heapq.heappush(tmp_classes, classes[i][1])

print(tmp_classes)