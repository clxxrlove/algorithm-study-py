import sys
import heapq

N = int(sys.stdin.readline().rstrip())
lecture = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
lecture.sort(key=lambda x: (x[1], x[2]))

classes = [lecture[0][2]]
for i in range(1, N):
    if lecture[i][1] >= classes[0]:
        heapq.heappop(classes)
    heapq.heappush(classes, lecture[i][2])

print(len(classes))