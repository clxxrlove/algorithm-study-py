# https://www.acmicpc.net/problem/11399
import sys

N, M = map(int, sys.stdin.readline().split())
peoples = dict()
result = []

for _ in range(N):
    people = sys.stdin.readline().rstrip()
    peoples[people] = 0

for _ in range(M):
    people = sys.stdin.readline().rstrip()
    if people in peoples:
        result.append(people)

print(len(result))
for res in sorted(result):
    print(res)