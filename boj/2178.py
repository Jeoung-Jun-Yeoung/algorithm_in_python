from nis import maps
import sys
from collections import deque

input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
Check = [[False] * (M) for _ in range(N)]
Graph = [[False] * (M) for _ in range(N)]

for col in range(N):
    line = list(input())
    for row in range(M):
        if line[row] == '1':
            Graph[col][row] = True
# for row in Check:
#     print(row)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs(start_y, start_x):
    # cnt = 1
    Check[0][0] = True
    q = deque()
    q.append((start_y, start_x, 1))
    while len(q) > 0:
        y, x, d = q.popleft()

        if y == N - 1 and x == M - 1:
            return d
        nd = d + 1

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not Check[ny][nx] and Graph[ny][nx]:
                Check[ny][nx] = True
                print("ny,nx,nd : ", ny, nx, nd)
                q.append((ny, nx, nd))


print(bfs(0, 0))
