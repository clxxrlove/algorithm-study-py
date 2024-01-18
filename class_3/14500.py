import sys

N, M = map(int, sys.stdin.readline().split())  # N = y, M = x
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상 하 좌 우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 대각선 1시 5시 7시 11시
lx = [1, 1, -1, -1]
ly = [1, -1, -1, 1]

ans = 0


# 4x1 블록
def _shape_1(x, y):
    horizontal_x, vertical_y = x + 3, y + 3
    _sum, _result = 0, 0

    # 가로 바
    if 0 <= horizontal_x < M:
        for i in range(x, horizontal_x + 1):
            _sum += _map[y][i]

    _result, _sum = _sum, 0

    # 세로 바
    if 0 <= vertical_y < N:
        for j in range(y, vertical_y + 1):
            _sum += _map[j][x]

    return max(_result, _sum)


# 2x2 블록
def _shape_2(x, y):
    nx, ny = x + 2, y + 2
    _sum = 0

    if 0 <= nx < M and 0 <= ny < N:
        for i in range(x, nx):
            for j in range(y, ny):
                _sum += _map[j][i]

    return _sum


# ㅗ 블록
def _shape_3(x, y):
    _sum, _result = 0, 0

    if not (0 <= x < M and 0 <= y < N):
        return 0

    for e in range(4):
        _sum += _map[y][x]
        for d in range(4):
            if e == d:
                continue
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < M and 0 <= ny < N:
                _sum += _map[ny][nx]
            else:
                _sum = 0
                break
        _result, _sum = max(_result, _sum), 0

    return _result


# L 블록 ! 대칭 가능 8개 모양 나옴 !
def _shape_4(x, y):
    vertical, horizontal = 0, 0
    _result = 0

    if 1 <= x < (M - 1) and 0 <= y < N:
        horizontal += _map[y][x - 1]
        horizontal += _map[y][x]
        horizontal += _map[y][x + 1]

    if 1 <= y < (N - 1) and 0 <= x < M:
        vertical += _map[y - 1][x]
        vertical += _map[y][x]
        vertical += _map[y + 1][x]

    if vertical == 0 and horizontal == 0:
        return 0

    for d in range(4):
        nx, ny = x + lx[d], y + ly[d]
        if 0 <= nx < M and 0 <= ny < N:
            _result = max(_result, _map[ny][nx])

    return _result + max(vertical, horizontal)


# ㄹ 블록
def _shape_5(x, y):
    _sum, _result = 0, 0

    # 1시 대각
    if 0 <= x + 1 < M and 0 <= y + 1 < N:
        tmp = 0
        _sum += _map[y + 1][x + 1]
        # 위
        if 0 <= y + 2 < N:
            tmp = _map[y + 2][x + 1] + _map[y + 1][x]
        # 오른쪽
        if 0 <= x + 2 < M:
            tmp = max(tmp, _map[y + 1][x + 2] + _map[y][x + 1])
        _sum += tmp

    _result, _sum = max(_result, _sum), 0

    # 5시 대각
    if 0 <= x + 1 < M and 0 <= y - 1 < N:
        tmp = 0
        _sum += _map[y - 1][x + 1]

        # 아래
        if 0 <= y - 2 < N:
            tmp = _map[y - 2][x + 1] + _map[y - 1][x]
        # 오른쪽
        if 0 <= x + 2 < M:
            tmp = max(tmp, _map[y - 1][x + 2] + _map[y][x + 1])
        _sum += tmp

    _result, _sum = max(_result, _sum), 0

    # 7시 대각
    if 0 <= x - 1 < M and 0 <= y - 1 < N:
        tmp = 0
        _sum += _map[y - 1][x - 1]

        # 아래
        if 0 <= y - 2 < N:
            tmp = _map[y - 2][x - 1] + _map[y - 1][x]
        # 왼쪽
        if 0 <= x - 2 < M:
            tmp = max(tmp, _map[y - 1][x - 2] + _map[y][x - 1])
        _sum += tmp

    _result, _sum = max(_result, _sum), 0

    # 11시 대각
    if 0 <= x - 1 < M and 0 <= y + 1 < N:
        tmp = 0
        _sum += _map[y + 1][x - 1]

        # 위
        if 0 <= y + 2 < N:
            tmp = _map[y + 2][x - 1] + _map[y + 1][x]
        # 왼쪽
        if 0 <= x - 2 < M:
            tmp = max(tmp, _map[y + 1][x - 2] + _map[y][x - 1])
        _sum += tmp

    _result = max(_result, _sum)

    if _result > 0:
        _result += _map[y][x]

    return _result


for i in range(N):
    for j in range(M):
        shape1 = _shape_1(j, i)
        shape2 = _shape_2(j, i)
        shape3 = _shape_3(j, i)
        shape4 = _shape_4(j, i)
        shape5 = _shape_5(j, i)
        ans = max(ans, shape1, shape2, shape3, shape4, shape5)

print(ans)
