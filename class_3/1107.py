# https://www.acmicpc.net/problem/1107
import sys
from itertools import product
from functools import reduce

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
buttons = [i for i in range(0, 10)]

if M == 10:
    print(abs(N - 100))
    exit(0)

broken = list(map(int, sys.stdin.readline().split())) if M else []

for b in broken:
    buttons.remove(b)

N_len = len(str(N))
ans = abs(N - 100)

for i in range(N_len - 1 if N_len > 1 else 1, N_len + 2):
    for p in product(buttons, repeat=i):
        tmp = reduce(lambda x, y: x * 10 + y, p)
        if tmp > 1000000:
            break
        tmp = abs(tmp - N) + len(str(tmp))
        ans = min(ans, tmp)

print(ans)