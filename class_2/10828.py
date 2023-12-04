# https://www.acmicpc.net/problem/10828
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
stack = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command.find(" ") != -1:
        A, B = command.split()
        stack.append(int(B))
    if command == "top":
        print(-1 if len(stack) == 0 else stack[-1])
    if command == "size":
        print(len(stack))
    if command == "empty":
        print(1 if len(stack) == 0 else 0)
    if command == "pop":
        print(-1 if len(stack) == 0 else stack.pop())
