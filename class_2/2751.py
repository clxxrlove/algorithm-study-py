# https://www.acmicpc.net/problem/2751
import sys

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

for num in sorted(nums):
    print(num)