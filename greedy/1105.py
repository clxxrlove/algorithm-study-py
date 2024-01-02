# https://www.acmicpc.net/problem/1105
import sys

L, R = sys.stdin.readline().split()
iL, iR = int(L), int(R)
ans = 0

if len(L) < len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] != '8':
                continue
            ans += 1
        else:
            break
    print(ans)