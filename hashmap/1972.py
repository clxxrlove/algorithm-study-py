# https://www.acmicpc.net/problem/1972
import sys

while True:
    s = sys.stdin.readline().rstrip()
    surprise = dict()
    result = True
    if s == "*":
        break

    if len(s) > 2:
        for i in range(len(s) - 2):
            surprise.clear()
            if result:
                for j in range(len(s) - 1 - i):
                    pair = s[j] + s[i + j + 1]
                    if pair in surprise:
                        result = False
                    else:
                        surprise[pair] = 1

    if result:
        print(f"%s is surprising." % s)
    else:
        print(f"%s is NOT surprising." % s)
