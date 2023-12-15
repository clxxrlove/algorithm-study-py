# https://www.acmicpc.net/problem/5585
import sys

N = int(sys.stdin.readline().rstrip())
money = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
result = 0

for coin in coins:
    result += money // coin
    money %= coin

print(result)