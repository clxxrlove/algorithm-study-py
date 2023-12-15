import sys

start = sys.stdin.readline().rstrip()

sx, sy = ord(start[0]) - 97, int(start[1]) - 1
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
result = 0

for move in moves:
    x, y = sx + move[0], sy + move[1]
    if 0 <= x < 8 and 0 <= y < 8:
        result += 1

print(result)