# https://www.acmicpc.net/problem/7576
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().rstrip())
heap = PriorityQueue()

for _ in range(N):
    command = int(sys.stdin.readline().rstrip())

    if command == 0:
        print(0 if heap.qsize() == 0 else -heap.get())
    else:
        heap.put(-command)