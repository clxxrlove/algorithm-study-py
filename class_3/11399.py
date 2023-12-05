# https://www.acmicpc.net/problem/11399
import sys

N = int(sys.stdin.readline().rstrip())
peoples = list(map(int, sys.stdin.readline().split()))
result, tmp = 0, 0

for people in sorted(peoples):
    result += tmp + people
    tmp += people

print(result)