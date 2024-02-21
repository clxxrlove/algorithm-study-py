import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, list(sys.stdin.readline().rstrip())))
ans = []

for num in nums:
    while ans and ans[-1] < num and K > 0:
        ans.pop()
        K -= 1
    ans.append(num)

for i in range(len(ans) - K):
    print(ans[i], end="")