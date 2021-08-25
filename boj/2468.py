from sys import stdin
from collections import deque, defaultdict
import copy

n = int(stdin.readline())
origin = []
dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]

m = 0

for i in range(n):
    line = list(map(int,stdin.readline().split()))
    temp = max(line)
    if temp > m:
        m = temp
    origin.append(line)


coun_list = []
graph = []

for k in range(m):
    temp_graph = copy.deepcopy((origin))
    for i in range(n):
        for j in range(n):
            temp_graph[i][j] = temp_graph[i][j] - k
            if temp_graph[i][j] <= 0:
                temp_graph[i][j] = 0
            else:
                temp_graph[i][j] = 1
                
    graph.append(temp_graph)


for i in range(len(graph)):
    dq = deque([])
    visted = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[i][x][y] == 1 and visted[x][y] == 0:
                visted[x][y] = 1
                cnt += 1
                dq.append([x,y])
                while dq:
                    cur_x,cur_y = dq.popleft()
                    for index in range(4):
                        nx = cur_x + dx[index]
                        ny = cur_y + dy[index]
                        if nx >= 0 and ny >= 0 and nx < n and ny < n:
                            if graph[i][nx][ny] == 1 and visted[nx][ny] == 0:
                                dq.append([nx,ny])
                                visted[nx][ny] = 1
    coun_list.append(cnt)
print(max(coun_list))
