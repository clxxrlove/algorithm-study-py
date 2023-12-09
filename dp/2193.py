# https://www.acmicpc.net/problem/2193
import sys

N = int(sys.stdin.readline().rstrip())
d = [0] * 91
fibo = [0] * 91
fibo[1], fibo[2] = 1, 1
d[1], d[2] = 1, 1

for i in range(2, N + 1):
    fibo[i] = (fibo[i - 1] + fibo[i - 2])

for n in range(2, N + 1):
    d[n] = d[n - 1] + fibo[n - 2]

print(d[N])