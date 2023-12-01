# https://www.acmicpc.net/problem/1259
import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().split()))

print(sum(M) / (max(M) * N) * 100)