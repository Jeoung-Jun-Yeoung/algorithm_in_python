from collections import deque

import sys

input = sys.stdin.readline

N, P = map(int, input().split())


stack = [[] for _ in range(7)]

ans = 0

for _ in range(N):
    line, plat = map(int, input().split())

    while stack[line] and stack[line][-1] > plat:
        stack[line].pop()
        ans += 1
    if stack[line] and stack[line][-1] == plat:
        continue
    stack[line].append(plat)
    ans += 1

print(ans)
