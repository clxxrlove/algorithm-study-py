import sys

N = int(sys.stdin.readline().rstrip())
X, Y = [], []
ans = 0

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
X.append(X[0])
Y.append(Y[0])

for i in range(N):
    ans += X[i] * Y[i + 1]
    ans -= X[i + 1] * Y[i]

print(abs(ans / 2))