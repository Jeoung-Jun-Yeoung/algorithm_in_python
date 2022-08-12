from sys import stdin
from collections import deque, defaultdict

n, m = map(int, stdin.readline().split())

graph = defaultdict(list)
visted = [False] * (n + 1)


def bfs(start):
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


ck = 0

for i in range(1, n+1):
    if not visted[i]:
        visted[i] = True
        ck += 1
        bfs(i)

print(ck)
