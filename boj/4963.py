from sys import stdin
from collections import deque, defaultdict
import copy

dy = [1,-1,0,0,1,1,-1,-1] # 상하좌우대각
dx = [0,0,-1,1,1,-1,1,-1]

while True:
    w, h = map(int,stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    visted = [[0 for _ in range(w)] for _ in range(h)]
    Map = []

    for i in range(h):
        part_of_map = list(map(int,stdin.readline().split()))
        Map.append(part_of_map)
    
    dq = deque([])
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                if visted[i][j] == 1:
                    continue
                dq.append([i,j])
                while dq:
                    y,x = dq.popleft()
                    
                    if visted[y][x] == 0:
                        visted[y][x] = 1
                        cnt += 1
                    for index in range(8):
                        ny = y + dy[index]
                        nx = x + dx[index]
                        if nx >= 0 and ny >= 0 and nx < w and ny < h:
                            if Map[ny][nx] == 1 and visted[ny][nx] == 0:
                                dq.append([ny,nx])
                                visted[ny][nx] = 1
                                    
    print(cnt)
