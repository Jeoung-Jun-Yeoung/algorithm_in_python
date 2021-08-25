from sys import stdin
from collections import deque, defaultdict


n = int(stdin.readline())
graph = defaultdict(list)
n1,n2 = map(int,stdin.readline().split())
visted = [False] * (n + 1)
cnt = int(stdin.readline())

depth = 0

for i in range(cnt):
    temp_n1, temp_n2 = map(int,stdin.readline().split())
    graph[temp_n1].append(temp_n2)
    graph[temp_n2].append(temp_n1)


dq = deque([])
dq.append([1,depth])
while dq:
    node,cur_depth = dq.popleft()
    if visted[node] == True:
        continue
    visted[node] = True
    dq.extend([graph[node],depth+1])
    print(depth)