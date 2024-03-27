import sys


def check(i, vertical=True):
    arr = []

    if vertical:
        arr = board[i]
    else:
        for k in range(N):
            arr.append(board[k][i])

    runway = False
    count = 0
    previous = arr[0] if arr else -1

    for a in arr:
        if runway and count >= L:
            runway = False
            count = 0

        if a == previous:
            count += 1
            previous = a
            continue

        if abs(a - previous) != 1:
            return False

        if a > previous: # 상승 -> 이 경우에는 이전이 무조건 runway -> False어도 맞음
            if runway:
                return False
            if count < L:
                return False
            count = 1
        elif a < previous: # 하강
            if runway:
                return False
            runway = True
            count = 1

        previous = a

    if runway:
        if count < L:
            return False

    # # runway일때 일정 카운트 만족시키면 초기화 시키도록 해야함 -> 중복 경사로 고려해야함
    # for a in arr:
    #     if a == previous:
    #         count += 1
    #     elif a > previous: # 이전까지가 경사로인 경우 (상승 경사로)
    #         if count >= L: # 경사로 끝
    #             runway = False
    #             count = 1 # 경사로 중첩 방지 로직
    #             previous = a
    #             continue
    #         else:
    #             return False # 조건 불일치
    #     else: # 이제부터 경사로인 경우 / 이전이 경사로었는가?
    #         if runway: # 이전까지가 경사로인 경우 (하강 경사로)
    #             if count < L:
    #                 return False
    #
    #         runway = True
    #         count = 1
    #
    #     previous = a

    return True


def solution():
    result = 0

    for i in range(N):
        if check(i):
            result += 1
        if check(i, False):
            result += 1

    return result


N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = solution()
print(answer)