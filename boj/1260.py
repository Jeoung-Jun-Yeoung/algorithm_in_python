from sys import stdin
from collections import deque, defaultdict

n, m, s = map(int, stdin.readline().split())

graph = defaultdict(list)

for i in range(m):
    n1, n2 = map(int, stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for key in graph.keys():
    graph[key].sort()

bfs_visited = [0 for _ in range(n + 1)]
rst = []
dq = deque([s])

while dq:
    node = dq.popleft()
    if bfs_visited[node] == 1:
        continue
    bfs_visited[node] = 1
    rst.append(node)
    dq.extend(graph[node])

dfs_visited = [0 for _ in range(n + 1)]

dfs_rst = []
stack = [s]

while stack:
    node = stack.pop()
    if dfs_visited[node] == 1:
        continue
    dfs_visited[node] = 1
    dfs_rst.append(node)
    stack.extend(sorted(graph[node], reverse=True))
print(dfs_rst)
print(rst)
