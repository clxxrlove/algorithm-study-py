# https://www.acmicpc.net/problem/10816
import sys

N = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().split()))
hashMap = dict()
result = list()

for card in cards:
    if card in hashMap:
        hashMap[card] += 1
    else:
        hashMap[card] = 1

for target in targets:
    if target in hashMap:
        result.append(hashMap[target])
    else:
        result.append(0)

print(*result)