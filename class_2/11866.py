# https://www.acmicpc.net/problem/11816
import sys

N, K = map(int, sys.stdin.readline().split())
seq = [i + 1 for i in range(N)]
result = []
loc = 0

while len(seq) > 0:
    loc += K - 1
    while loc >= len(seq):
        loc -= len(seq)

    result.append(seq[loc])
    del seq[loc]

print("<" + ", ".join(map(str, result)) + ">")