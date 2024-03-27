import sys


def toString(arr):
    return ''.join(arr)


def solution(s, b):
    stack = []
    bomb_length = len(b)

    for char in s:
        stack.append(char)

        if toString(stack[-bomb_length:]) == b:
            for _ in range(bomb_length):
                stack.pop()

    if stack:
        return toString(stack)
    return "FRULA"


string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

answer = solution(string, bomb)
print(answer)