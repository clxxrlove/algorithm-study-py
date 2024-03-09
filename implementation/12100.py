import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline().rstrip())
ans = 0

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def horizon(arr, xrange):
    for y in range(N):
        tmp, tmp_index = -1, -1
        for x in xrange:
            if arr[y][x] == tmp:
                arr[y][tmp_index] *= 2
                arr[y][x] = 0
                tmp, tmp_index = -1, -1
            elif arr[y][x] != 0:
                tmp, tmp_index = arr[y][x], x

    return arr


def left(arr):
    arr = horizon(arr, range(N))
    for y in range(N):
        ty = list(filter(lambda x: x != 0, arr[y]))
        ty += [0] * (N - len(ty))
        arr[y] = ty

    return arr


def right(arr):
    arr = horizon(arr, range(N - 1, -1, -1))
    for y in range(N):
        ty = list(filter(lambda x: x != 0, arr[y]))
        arr[y] = [0] * (N - len(ty)) + ty

    return arr


def vertical(arr, yrange):
    for x in range(N):
        tmp, tmp_index = -1, -1
        for y in yrange:
            if arr[y][x] == tmp:
                arr[tmp_index][x] *= 2
                arr[y][x] = 0
                tmp, tmp_index = -1, -1
            elif arr[y][x] != 0:
                tmp, tmp_index = arr[y][x], y

    return arr


def up(arr):
    arr = vertical(arr, range(N))
    for x in range(N):
        ty = []
        for y in range(N):
            ty.append(arr[y][x])

        ty = list(filter(lambda x: x != 0, ty))
        ty += [0] * (N - len(ty))

        for y in range(N):
            arr[y][x] = ty[y]

    return arr


def down(arr):
    arr = vertical(arr, range(N - 1, -1, -1))
    for x in range(N):
        ty = []
        for y in range(N):
            ty.append(arr[y][x])

        ty = list(filter(lambda x: x != 0, ty))
        ty = [0] * (N - len(ty)) + ty

        for y in range(N):
            arr[y][x] = ty[y]

    return arr


def deepcopy(arr):
    return [item[:] for item in arr]


def backtracking(depth, arr):
    global ans

    if depth == 5:
        value = 0
        for i in range(N):
            value = max(value, max(arr[i]))

        ans = max(ans, value)
        return

    for i in range(4):
        copied = deepcopy(arr)
        if i == 0:
            backtracking(depth + 1, left(copied))
        elif i == 1:
            backtracking(depth + 1, right(copied))
        elif i == 2:
            backtracking(depth + 1, up(copied))
        else:
            backtracking(depth + 1, down(copied))


backtracking(0, board)
print(ans)