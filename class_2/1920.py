# https://www.acmicpc.net/problem/1920
import sys


def bin_search(arr, start, end, target):
    if start > end:
        return 0
    mid = (end + start) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return bin_search(arr, start, mid - 1, target)
    else:
        return bin_search(arr, mid + 1, end, target)


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))
A = sorted(A)

for b in B:
    print(bin_search(A, 0, N - 1, b))