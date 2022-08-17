import sys

input = sys.stdin.readline

cache = [-1] * 91
cache[0] = 0
cache[1] = 1
N = int(input())

for i in range(2, N+1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[N])
