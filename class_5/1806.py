import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = arr[0]
ans = 1e9

s, e = 0, 0

while True:
    if result < S:
        e += 1
        if e == N:
            break
        result += arr[e]
    else:
        result -= arr[s]
        ans = min(ans, e - s + 1)
        s += 1

print(ans if ans != 1e9 else 0)