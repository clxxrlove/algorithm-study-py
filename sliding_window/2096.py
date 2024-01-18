# DP
import sys

N = int(sys.stdin.readline().rstrip())
min_value = [0, 0, 0]
max_value = [0, 0, 0]


def calc(arr, op, f):
    tmp = arr[:]
    arr[0] = f(tmp[0], tmp[1]) + op[0]
    arr[1] = f(tmp[0], tmp[1], tmp[2]) + op[1]
    arr[2] = f(tmp[1], tmp[2]) + op[2]


for _ in range(N):
    operator = list(map(int, sys.stdin.readline().split()))
    calc(min_value, operator, min)
    calc(max_value, operator, max)

print(max(max_value), min(min_value))