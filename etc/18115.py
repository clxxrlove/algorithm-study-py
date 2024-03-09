import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))
cards.reverse()

q = deque()
for i in range(N):
    if cards[i] == 1:
        q.appendleft(i + 1)
    elif cards[i] == 2:
        q.insert(1, i + 1)
    elif cards[i] == 3:
        q.append(i + 1)

print(*q)