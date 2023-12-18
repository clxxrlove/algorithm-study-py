# https://www.acmicpc.net/problem/1931
import sys

N = int(sys.stdin.readline().rstrip())
meetings = []
result = []

for _ in range(N):
    meeting = tuple(map(int, sys.stdin.readline().split()))
    meetings.append(meeting)

meetings.sort()

for meeting in meetings:
    if len(result) > 0:
        if result[-1][1] >= meeting[1]:
            if meeting[0] == meeting[1] and meeting[1] == result[-1][1]:
                result.append(meeting)
                continue
            result.pop()
            result.append(meeting)
        elif result[-1][1] <= meeting[0]:
            result.append(meeting)
    else:
        result.append(meeting)

print(len(result))