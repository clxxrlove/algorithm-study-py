import sys
from collections import deque

N, M, y, x, K = map(int, sys.stdin.readline().split()) # 세로 가로
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = list(map(int, sys.stdin.readline().split()))
dice = [[-1, 0, -1], deque([0, 0, 0]), [-1, 0, -1], [-1, 0, -1]] # 더미는 -1로 초기화
direction = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 그래프 기준 "방향으로" 동, 서, 북, 남 (x, y)
dice_x, dice_y = 1, 1


def roll_dice2(dice, command): # 조금 더 근본적으로 주사위를 굴림
    if command <= 2: # 좌 우 회전의 경우
        dice[1].rotate(-1 if command == 1 else 1)
        dice[3][1], dice[1][2 if command == 1 else 0] = dice[1][2 if command == 1 else 0], dice[3][1]
    else:
        if command == 4:
            for i in range(1, 4):
                dice[i - 1][1], dice[i][1] = dice[i][1], dice[i - 1][1]
        else:
            for i in range(3, 0, -1):
                dice[i - 1][1], dice[i][1] = dice[i][1], dice[i - 1][1]


# def adapt_direction(direction):
#
#
#
# def roll_dice(x, y, command):
#     dx, dy = x + direction[command][0], y + direction[command][1]
#
#     if 0 <= dx < 3 and 0 <= dy < 4 and _map[dy][dx] != -1: # 좌표도 맞고 더미도 아닌 경우 (제대로 굴림)
#         return dx, dy
#     return find_cur(x, y, dx, dy)
#
#
# def find_cur(x, y, dx, dy): # 굴리기 전 위치 제외 -1이 아닌 곳 찾음 // 그래프 그대로 방향 이동 하려면 방향 제대로 잡아야 함
#     qx, qy = 0, 0
#
#     for d in direction:
#         nx, ny = dx + d[0], dy + d[1]
#         if 0 <= dx < 3 and 0 <= dy < 4: # 이미 굴린 시점에서 위치 판단
#             if nx < 0 or nx >= 3 or ny < 0 or ny >= 4: # 굴려진 시점에서 밖으로 나가는 건 의미 X
#                 continue
#             if nx == x and ny == y:
#                 continue
#             if _map[ny][nx] != -1: # 정수를 만나면 얘가 우선임
#                 return nx, ny
#             else:
#                 if qx == 0 and qy == 0: # 아직 정수를 마주치지 않은 경우, 얘는 한 번 더 굴려야 함
#                     qx, qy = nx, ny
#         else: # 정상적으로 굴려진 상황
#             return dx % 3, dy % 4
#
#     return find_cur(dx, dy, qx, qy)
#
#
# def fill_dice(): # 내 위치 기준 천장 구하기
#     pass


for c in commands:
    dx, dy = x + direction[c - 1][0], y + direction[c - 1][1]

    if dx < 0 or dx >= M or dy < 0 or dy >= N:
        continue

    x, y = dx, dy
    roll_dice2(dice, c)
    if _map[y][x] == 0:
        _map[y][x] = dice[1][1]
    else:
        dice[1][1], _map[y][x] = _map[y][x], 0
    print(dice[3][1])