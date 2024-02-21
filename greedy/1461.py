import sys

N, M = map(int, sys.stdin.readline().split())
ans = 0

pos = list(map(int, sys.stdin.readline().split()))
pos.sort(key=lambda x: abs(x))

p_pos = list(filter(lambda x: x > 0, pos))
m_pos = list(filter(lambda x: x < 0, pos))

while p_pos or m_pos:
    if p_pos and m_pos:
        if p_pos[-1] > -m_pos[-1]:
            ans += p_pos[-1] * 2
            p_pos = p_pos[:-M]
        else:
            ans -= m_pos[-1] * 2
            m_pos = m_pos[:-M]
    elif p_pos:
        ans += p_pos[-1] * 2
        p_pos = p_pos[:-M]
    else:
        ans -= m_pos[-1] * 2
        m_pos = m_pos[:-M]

print(ans - abs(pos[-1]))