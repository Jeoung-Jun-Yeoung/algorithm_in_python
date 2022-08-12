import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[False] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = True


def dfs(now):
    for next in range(N):
        if adj[now][next]:
            dfs(next)
    cnt += 1
