# https://www.acmicpc.net/problem/14891
import sys
from collections import deque

gears = [[]] + [deque(list(map(int, sys.stdin.readline().rstrip()))) for _ in range(4)]
K = int(sys.stdin.readline().rstrip())
moves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
result = 0

for move in moves:
    direction = move[1] * -1
    r, l = direction, direction
    gears[move[0]].rotate(move[1])

    for i in range(move[0] + 1, 5):  # 다음 바퀴 부터 4까지
        if gears[i][6] == gears[i - 1][2 - r]:
            break
        else:
            gears[i].rotate(r)
            r *= -1

    for i in range(move[0] - 1, 0, -1):  # 이전 바퀴 부터 1까지
        if gears[i][2] == gears[i + 1][6 - l]:
            break
        else:
            gears[i].rotate(l)
            l *= -1

for i in range(1, 5):
    if gears[i][0] == 1:
        result += 2 ** (i - 1)

print(result)