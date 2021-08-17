from sys import stdin
from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10000)


def dfs(node):
    visted[node] = 1
    for i in graph[node]:
        if not visted[i]:
            dfs(i)


n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visted = [[False] for _ in range(n + 1)]

for i in range(m):
    x, y = list(map(int, stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

ck = 0


for i in range(n):
    if not visted[i]:
        dfs(i)
        ck += 1
print(ck)
