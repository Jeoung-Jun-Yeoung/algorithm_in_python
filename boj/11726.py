from functools import cache
import sys

input = sys.stdin.readline
MOD = 10007
cache = [0] * 1001
cache[1] = 1
cache[2] = 2
cache[3] = 3

n = int(input())
n = n

for i in range(4, 1001):
    cache[i] = cache[i - 1] * 1 + cache[i - 2] * 1

print(cache[n] % MOD)
