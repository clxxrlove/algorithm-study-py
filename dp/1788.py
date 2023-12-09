# https://www.acmicpc.net/problem/1788
import sys

N = int(sys.stdin.readline().rstrip())
num = [0] * 2000001
num[1] = 1
num[-1] = 1

if N > 1:
    for i in range(2, N + 1):
        num[i] = (num[i - 1] + num[i - 2]) % 1000000000
elif N < -1:
    for i in range(-2, N - 1, -1):
        num[i] = (num[i + 2] - num[i + 1])
        if num[i] > 0:
            num[i] = num[i] % 1000000000
        else:
            num[i] = num[i] % -1000000000

if num[N] > 0:
    print(1)
elif num[N] == 0:
    print(0)
else:
    print(-1)
print(abs(num[N]))