import sys
input = sys.stdin.readline

N, X = map(int, input().split())
views = list(map(int, input().split()))

ans = [sum(views[0:X])]

for i in range(X, N):
    ans.append(ans[-1] - views[i - X] + views[i])

if max(ans) > 0:
    print(max(ans))
    print(ans.count(max(ans)))
else:
    print("SAD")