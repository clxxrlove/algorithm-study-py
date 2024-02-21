import sys

while True:
    string = sys.stdin.readline().rstrip()
    stack = []
    if string == ".":
        break

    for s in string:
        if s not in "()[]":
            continue
        if s == ")":
            if len(stack) == 0 or stack[-1] != "(":
                stack.append(1)
                break
            stack.pop()
        elif s == "]":
            if len(stack) == 0 or stack[-1] != "[":
                stack.append(1)
                break
            stack.pop()
        else:
            stack.append(s)

    print("no" if len(stack) else "yes")