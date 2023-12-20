# https://www.acmicpc.net/problem/9663
import sys

N = int(sys.stdin.readline().rstrip())
queens = []
count = 0
visited = [False] * N


def check(x, y):
    for queen in queens:
        dx = abs(queen[0] - x)
        dy = abs(queen[1] - y)
        if dx == dy or queen[0] == x or queen[1] == y:
            return False

    return True


def backtracking(x):
    global count

    if len(queens) == N:
        count += 1
        return

    for i in range(N):
        if not visited[i]:
            if check(x, i):
                queens.append((x, i))
                visited[i] = True
                backtracking(x + 1)
                visited[i] = False
                queens.pop()


backtracking(0)
print(count)