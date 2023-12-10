# https://www.acmicpc.net/problem/1927
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().rstrip())
pq = PriorityQueue(maxsize=N)

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        pq.put(x)
    else:
        if pq.qsize() == 0:
            print(0)
        else:
            print(pq.get())
