# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    raw_arr = sys.stdin.readline().rstrip()
    arr = deque(raw_arr[1:-1].split(",")) if N != 0 else []

    reverse = False
    error = False

    for command in p:
        if command == "R":
            reverse = not reverse
        else:
            if len(arr) == 0:
                error = not error
                break

            if reverse:
                arr.pop()
            else:
                arr.popleft()

    result = ",".join(reversed(arr) if reverse else arr)
    print("[" + result + "]" if not error else "error")
