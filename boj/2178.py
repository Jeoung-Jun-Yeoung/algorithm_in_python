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
    cnt = 0
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        if y == N - 1 and x == M - 1:
            break
        Check[y][x] = True
        cnt += 1
        flag = False
        for k in range(4):
            in_cnt = 0
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not Check[ny][nx]:
                if Graph[ny][nx]:
                    flag = True
                    in_cnt += 1
                    print("ny nx", ny, nx)
                    q.append((ny, nx))
        if not flag or in_cnt > 1:
            cnt -= 1
        print()
    print(cnt)


bfs(0, 0)
