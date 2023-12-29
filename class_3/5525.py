# https://www.acmicpc.net/problem/5525
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

bench = 2 * N
progress = 0
ans = 0

for i in range(0, M - 1):
    if S[i] != S[i + 1]:
        if progress > 0:
            progress += 1
        else:
            if S[i] == "I":
                progress = 1
    else:
        while progress >= bench:
            ans += 1
            progress -= 2
        progress = 0

while progress >= bench:
    ans += 1
    progress -= 2

print(ans)