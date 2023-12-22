# https://www.acmicpc.net/problem/19583
import sys

S, E, Q = sys.stdin.readline().split()
attendance = dict()
count = 0

for line in sys.stdin:
    time, nickname = line.split()

    if S >= time:
        attendance[nickname] = 1 # 1은 제대로 출석한 애들

    if E <= time <= Q:
        if nickname in attendance:
            if attendance[nickname] == 1:
                attendance[nickname] = 2 # 2는 잘 끝낸 애들 and 중복 방지
                count += 1

print(count)