from sys import stdin
from pprint import pprint
from collections import defaultdict, deque

t = int(stdin.readline())

dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]

for case in range(t):

    row, col, target = map(int, stdin.readline().split())

    graph = [[0 for _ in range(row)] for _ in range(col)]
    visted = [[0 for _ in range(row)] for _ in range(col)]
    
    dq = deque([])
    temp_dq = deque([])
    ck = 0
    for i in range(target):
        x, y = list(map(int, stdin.readline().split()))
        graph[y][x] = 1
        dq.append([y, x])

    for i in range(target):
        y, x = dq.popleft()
        if visted[y][x] == 0:
            visted[y][x] = 1
            temp_dq.append([y,x])
            ck += 1
            while temp_dq:
                y,x = temp_dq.popleft()
                for i in range(4):
                    ny,nx = y+dy[i],x+dx[i]
                    if ny >= 0 and nx >= 0 and ny < col and nx < row:
                        if graph[ny][nx] == 1 and visted[ny][nx] == 0:
                            temp_dq.append([ny,nx])
                            visted[ny][nx] = 1
    print(ck)