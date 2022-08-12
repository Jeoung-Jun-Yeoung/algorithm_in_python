import sys
from collections import deque

input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
Check = [[False] * (M) for _ in range(N)]

for col in range(N):
    line = list(input())
    print("ck", line)
    for row in range(M):
        if line[row] == 1:
            Check[col][row] = True
for row in Check:
    print(row)
