# https://www.acmicpc.net/problem/1920
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
cards = deque([i for i in range(1, N + 1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])