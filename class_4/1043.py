import sys

N, M = map(int, sys.stdin.readline().split())
truth = set(map(int, sys.stdin.readline().split()[1:]))
parties = []

for _ in range(M):
    party = set(map(int, sys.stdin.readline().split()[1:]))
    parties.append(party)

for _ in range(M):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

ans = 0
for party in parties:
    if not party & truth:
        ans += 1

print(ans)