from sys import gettrace, stdin
from collections import deque, defaultdict


n = int(stdin.readline())

visted = [False] * (n + 1)
dq = deque([])
graph = defaultdict(list)
depth = 0

conect = defaultdict(int)

for i in range(n-1):
    n1, n2 = map(int, stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for key in graph.keys():
    graph[key].sort()
    # sort 이유

anw = defaultdict(int)

dq = deque([[1,depth]])

while dq:   
    node,pnode = dq.popleft()
    anw[node] = pnode
    if visted[node] == 1:
        continue
    visted[node] = 1

    for i in graph[node]:
        if visted[i] == 1:
            continue
        dq.append([i,node])



for i in range(2,n+1):
    print(anw[i])