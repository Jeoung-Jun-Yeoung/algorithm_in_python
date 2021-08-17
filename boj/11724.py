from sys import stdin
<<<<<<< HEAD
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
=======
from collections import deque,defaultdict

n,m = map(int,stdin.readline().split())

graph = defaultdict(list)

def dfs(start):
    visted[start] = True
    for i in range(1,n+1):
        if visted[start] != False and graph[start][i] == 1:
            dfs(i)


for i in range(m):
    n1,n2 = map(int,stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visted = [False] * (n + 1)

ck = 0

for i in range(1,n+1):
    if not visted[i]:
        dfs(i)
        print(visted)
        ck += 1
    print(ck)

print(ck)


>>>>>>> 5b4d40da5e2abad2a911f80dad78ebfb3928c1ba
