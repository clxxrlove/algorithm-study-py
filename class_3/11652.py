# https://www.acmicpc.net/problem/1012
import sys

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
cards = dict()

for n in nums:
    if n in cards:
        cards[n] += 1
    else:
        cards[n] = 1

sorted_cards = sorted(cards.items(), key=lambda x: x[1], reverse=True)
result = []
crit = max(cards.values())

for sc in sorted_cards:
    if sc[1] == crit:
        result.append(sc[0])

print(min(result))