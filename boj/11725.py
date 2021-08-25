from sys import gettrace, stdin
from collections import deque, defaultdict


n = int(stdin.readline())

visted = [False] * (n + 1)
dq = deque([])
graph = defaultdict(list)
depth = 0

for i in range(n-1):
    n1, n2 = map(int, stdin.readline().split())
    graph[n1,depth].append(n2)
    graph[n2,depth].append(n1)

for key in graph.keys():
    graph[key].sort()
    # sort 이유
print('g',graph)


dq = deque([1,depth])
while dq:
    print('dq',dq)
    node = dq.popleft()
    print('node',node)
    if visted[node] == 1:
        continue
    visted[node] = 1
    dq.extend(graph[node,depth+1])
print(graph)