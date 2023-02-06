from itertools import combinations
from itertools import permutations
from collections import deque
import sys


sys.setrecursionlimit(10**6)


def dfs(v):
    # 탈출조건
    visited[v] = True
    for next in range(1, 4):
        if graph[next] and not visited[v][next]:
            dfs(next)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        p = q.popleft()
        for next in range(1, 4):
            if graph[next] and not visited[v][next]:
                visited[next] = True
                q.append(next)
