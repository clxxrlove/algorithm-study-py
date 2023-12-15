# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0

    while queue:
        important = max(queue)
        top = queue.popleft()

        if top == important:
            count += 1
            if M == 0:
                break
        else:
            queue.append(top)

        M -= 1
        if M < 0:
            M = len(queue) - 1

    print(count)
