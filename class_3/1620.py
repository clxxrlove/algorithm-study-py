# https://www.acmicpc.net/problem/1620
import sys

N, M = map(int, sys.stdin.readline().split())
pokemon = dict()
pokemonNumber = dict()

for i in range(N):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = str(i + 1)
    pokemonNumber[str(i + 1)] = name

for _ in range(M):
    quiz = sys.stdin.readline().rstrip()
    print(pokemon[quiz] if quiz in pokemon else pokemonNumber[quiz])