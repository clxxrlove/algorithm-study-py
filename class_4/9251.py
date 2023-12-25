# https://www.acmicpc.net/problem/9251
import sys

s1 = '-' + sys.stdin.readline().rstrip()
s2 = '-' + sys.stdin.readline().rstrip()
d = [[0] * (len(s2)) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[len(s1) - 1][len(s2) - 1])