from sys import stdin
from collections import defaultdict, deque

t = int(stdin.readline())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]


for i in range(t):
    dq = deque([])
    l = int(stdin.readline())
    x,y = map(int,stdin.readline().split())
    tx,ty = map(int,stdin.readline().split())

    graph = [[0 for _ in range(l)] for _ in range(l)]
    visted = [[0 for _ in range(l)] for _ in range(l)]
    cnt = 0
    dq.append([x,y,cnt])
    flag = 0
    while dq:
        x,y,cnt = dq.popleft()
        if x == tx and y == ty:
            print(cnt)
            break
        if visted[x][y] == 0:
            visted[x][y] = 1

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and ny >= 0 and nx < l and ny < l:
                    dq.append([nx,ny,cnt + 1])