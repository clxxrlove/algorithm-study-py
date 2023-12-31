# https://www.acmicpc.net/problem/6064
import sys


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def lcm(x, y):
    return x * y // gcd(x, y)


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    t_lcm = lcm(M, N)
    x_ans = x
    ans = False

    while t_lcm >= x_ans:
        tmp = (x_ans - 1) % N + 1
        if tmp == y:
            ans = True
            break
        x_ans += M

    if ans:
        print(x_ans)
    else:
        print(-1)