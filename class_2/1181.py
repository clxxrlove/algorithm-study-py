# https://www.acmicpc.net/problem/1181
import sys

N = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

for word in sorted(sorted(set(words)), key=len):
    print(word)