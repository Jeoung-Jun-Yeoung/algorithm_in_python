from collections import deque
from itertools import combinations
from itertools import permutations
import math
import sys


n = int(input())

picture = []


def is_valid_map(x, y):
    return (0 <= x < n) and (0 <= y < n)


dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


# COL
# ROW


def bfs(x, y):
    q = deque()
    q.append([x, y])

    visited[x][y] = True
    NowColor = picture[x][y]
    # print(f'Now Color {NowColor}')
    # 조건은 같은 색이면서, 맵안에 있으면 갈 수 있다.

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(f' x y {x,y} nx,ny {nx,ny}')
            if is_valid_map(nx, ny) and not visited[nx][ny]:
                # 맵안에 있으면서, 안가봄
                if NowColor == picture[nx][ny]:
                    # 거기에 색이 같다면
                    visited[nx][ny] = True
                    # 방문표시후 큐에 넣어주기
                    # if picture[nx][ny] == 'G':
                    #     picture[nx][ny] = 'R'

                    # 원본을 건들이면 안되나?하는 생각..? 미리 방문지도 바꾸면 안되는거 같음. 근데 이미 본곳은 바꿔도 되지 않나..
                    # 적록색약 보정 42 ~ 43 라인. 나 자신도 G였을테니까 이것도 바꿔줘야함
                    q.append([nx, ny])


for _ in range(n):
    picture.append(list(input()))


visited = [[False] * n for _ in range(n)]
total = 0
color = ['R', 'G', 'B']

for c in color:
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 여기서 일단 적록색약 아닌 사람이 본걸 새보자.
            if not visited[i][j] and picture[i][j] == c:
                # print(f'i,j {i,j} pC {picture[i][j]} c {c}')
                bfs(i, j)
                # for vi in visited:
                #     print(vi)
                cnt += 1
    total += cnt

# for p in picture:
#     print(p)
# 적록버전 체크 코드

for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
# 강제로 뒤집었다.

visited = [[False] * n for _ in range(n)]

wtotal = 0
for c in ['R', 'B']:
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 여기서 일단 적록색약 아닌 사람이 본걸 새보자.
            if not visited[i][j] and picture[i][j] == c:
                # print(f'i,j {i,j} pC {picture[i][j]} c {c}')
                bfs(i, j)
                # for vi in visited:
                #     print(vi)
                # print()
                cnt += 1

    wtotal += cnt
print(total, wtotal)
# 적록색약이 아닌 사람부터 샌다.
