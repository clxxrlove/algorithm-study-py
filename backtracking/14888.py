# https://www.acmicpc.net/problem/15663
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

maximum, minimum = float("-inf"), float("inf")


def dfs(depth, num, op):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return

    if op[0] > 0:
        op[0] -= 1
        dfs(depth + 1, num + nums[depth], op)
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(depth + 1, num - nums[depth], op)
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(depth + 1, num * nums[depth], op)
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        dfs(depth + 1, int(num / nums[depth]), op)
        op[3] += 1


dfs(1, nums[0], op)
print(maximum, minimum)