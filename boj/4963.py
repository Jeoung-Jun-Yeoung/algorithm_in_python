from sys import stdin
from collections import deque, defaultdict
import copy

dy = [1,-1,0,0,1,1,-1,-1] # 상하좌우대각
dx = [0,0,-1,1,1,-1,1,-1]

while True:
    w, h = map(int,stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = [[0 for _ in range(w)] for _ in range(h)]
    visted = [[0 for _ in range(w)] for _ in range(h)]
    Map = []
    cordinate = []
    for i in range(h):
        part_of_map = list(map(int,stdin.readline().split()))
        Map.append(part_of_map)
    dq = deque([])
    cnt = 0
    print(visted)
    print(Map)
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                print(i,j)
                dq.append([i,j])
                while dq:
                    x,y = dq.popleft()
                    print('x and y',x,y)
                    print(visted)
                    if visted[x][y] == 0:
                        visted[x][y] = 1
                        cnt += 1
                        for index in range(8):
                            nx = x + dx[index]
                            ny = y + dy[index]
                            if nx >= 0 and ny >= 0 and nx < w and ny < h:
                                if Map[nx][ny] == 1 and visted[nx][ny] == 0:
                                    dq.append([nx,ny])
                                    
    print(cnt)



    