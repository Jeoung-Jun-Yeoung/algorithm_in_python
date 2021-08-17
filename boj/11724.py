from sys import stdin
from collections import deque, defaultdict

n, m = map(int, stdin.readline().split())

graph = defaultdict(list)
visted = [False] * (n + 1)


def bfs(start):
    visted[start] = True
    dq = deque([start])
    while dq:
        node = dq.popleft()
        for i in graph[node]:
            if not visted[i]:
                dq.append(i)
                visted[i] = True


for i in range(m):
    n1, n2 = map(int, stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


print(graph)
ck = 0

for i in range(1, n+1):
    if not visted[i]:
        bfs(i)
        ck += 1
print(ck)
