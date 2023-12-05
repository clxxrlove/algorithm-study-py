# https://www.acmicpc.net/problem/11723
import sys

N = int(sys.stdin.readline().rstrip())
zz = [i for i in range(1, 21)]
ball = set()


for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command == "all":
        ball = set(zz)
    elif command == "empty":
        ball.clear()
    else:
        A, B = command.split()
        B = int(B)

        if A == "add":
            ball.add(B)
        elif A == "remove":
            if B in ball:
                ball.remove(B)
        elif A == "check":
            print(1 if B in ball else 0)
        elif A == "toggle":
            if B in ball:
                ball.remove(B)
            else:
                ball.add(B)