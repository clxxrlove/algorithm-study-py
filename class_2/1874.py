import sys

N = int(sys.stdin.readline().rstrip())
stack, seek = [], 1
ans = []

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    while seek <= n:
        stack.append(seek)
        ans.append("+")
        seek += 1
    if stack[-1] == n:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        exit()

for a in ans:
    print(a)