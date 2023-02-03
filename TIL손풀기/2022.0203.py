# bfs, dfs
from itertools import Counter
from collections import deque
import sys
sys.setrecursionlimit(10**6)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs(G, start):
    res, vis = [], [False] * len(G)

    Q = deque([start])

    vis[start] = True

    while(len(G)) != 0:
        v = Q.popleft()
        res.append(v)

        for u in G[v]:
            if not vis[u]:
                vis[u] = True
                Q.append(u)
    return res


def dfs(G, start):
    res, vis = [], [False] * len(G)

    def rec(v):
        vis[v] = True
        res.append(v)
        for u in G[v]:
            if not vis[u]:
                rec(u)
    rec(start)
    return res

# 가장 중요한것은 올바른 칸인지 확인하는것이다.


N = '가로'
M = '세로'


def is_valid_map(x, y, map):
    return x <= 0 or x > N or y > M or y <= 0
# 넣기전 이걸로 맵에 올바르게 있는지 판단한다.


map = [list(map(int, input().split())) for _ in range(int(input()))]

N, *arr = map(int, input().split())

arr = [list(input()) for _ in range(N)]

# 문자열 거꾸로

name[::-1]

val = Counter(arr).most_common()
