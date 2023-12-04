# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command.find("push_front") != -1:
        A, B = command.split()
        queue.appendleft(int(B))
    if command.find("push_back") != -1:
        A, B = command.split()
        queue.append(int(B))
    if command == "front":
        print(-1 if len(queue) == 0 else queue[0])
    if command == "back":
        print(-1 if len(queue) == 0 else queue[-1])
    if command == "size":
        print(len(queue))
    if command == "empty":
        print(1 if len(queue) == 0 else 0)
    if command == "pop_front":
        print(-1 if len(queue) == 0 else queue.popleft())
    if command == "pop_back":
        print(-1 if len(queue) == 0 else queue.pop())