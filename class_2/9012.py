# https://www.acmicpc.net/problem/9012
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

for n in range(N):
    bracket = sys.stdin.readline().rstrip()
    temp = deque()

    for b in bracket:
        if b == "(":
            temp.append(b)
        else:
            if len(temp) == 0:
                temp.append(1)
                break
            close = temp.pop()
            if close == ")":
                temp.append(1)
                break

    if len(temp) == 0:
        print("YES")
    else:
        print("NO")
