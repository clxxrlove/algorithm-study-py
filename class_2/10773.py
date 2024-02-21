import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))