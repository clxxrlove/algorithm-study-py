# https://www.acmicpc.net/problem/1541
import sys

expression = sys.stdin.readline().rstrip()
split = expression.split("-")
result = 0

if split[0] == expression:
    operand = expression.split("+")
    for op in operand:
        result += int(op)
else:
    operand = []
    for i, item in enumerate(split):
        if "+" in item:
            operand.extend(map(int, item.split("+")))
        else:
            operand.append(int(item))

        if i == 0:
            while len(operand) != 0:
                result += operand.pop()

    for op in operand:
        result -= op

print(result)