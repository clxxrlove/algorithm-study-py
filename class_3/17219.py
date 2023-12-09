# https://www.acmicpc.net/problem/17219
import sys

N, M = map(int, sys.stdin.readline().split())
sites = dict()

for n in range(N):
    site, pw = sys.stdin.readline().split()
    sites[site] = pw

for m in range(M):
    site = sys.stdin.readline().rstrip()
    print(sites[site])