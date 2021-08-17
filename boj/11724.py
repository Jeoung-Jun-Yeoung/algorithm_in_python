from sys import stdin
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


