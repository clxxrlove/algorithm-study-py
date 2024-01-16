import sys

N, M = map(int, sys.stdin.readline().split())

team = dict()

for i in range(N):
    team_name = sys.stdin.readline().rstrip()
    team_len = int(sys.stdin.readline().rstrip())
    team_members = [sys.stdin.readline().rstrip() for _ in range(team_len)]
    team[team_name] = sorted(team_members)

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    q_type = int(sys.stdin.readline().rstrip())

    if q_type == 0:
        print("\n".join(team[q]))
    else:
        for t in team.keys():
            if q in team[t]:
                print(t)