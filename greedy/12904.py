import sys

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

end = len(S)
start = len(T)

while True:
    if T[-1] == 'B':
        T.pop()
        T.reverse()
    else:
        T.pop()

    start -= 1

    if end == start:
        break

print(1 if S == T else 0)