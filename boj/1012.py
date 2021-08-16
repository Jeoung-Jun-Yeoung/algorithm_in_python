from sys import stdin
from collections import defaultdict, deque

t = int(stdin.readline())

col,row,target = map(int,stdin.readline().split()) 

graph = [[0 for _ in range(col + 1) ] for _ in range(row + 1)]
visted = [[0 for _ in range(col + 1) ] for _ in range(row + 1)]
dq = deque([])
temp_dq = deque([])

for i in range(target):
    x,y = list(map(int,stdin.readline().split()))
    graph[y][x] = 1
    dq.append([x,y])

ck = 0

while dq:
    temp = dq.popleft()
    x = temp[0]
    y = temp[1]
    if graph[y][x] == 1:
        if visted[y][x] != 1:
            visted[y][x] = 1
            temp_dq.append([x + 1,y])
            temp_dq.append([x - 1,y])
            temp_dq.append([x,y + 1])
            temp_dq.append([x,y - 1])
            while temp_dq:
                tmp = temp_dq.popleft()
                n1 = tmp[0]
                n2 = tmp[1]
                if graph[n1][n2]:
