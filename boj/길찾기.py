from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False] * 100 for _ in range(100)]

N = int(input())


def is_Valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True
        # 다음 좌표 후보는 4군데. 상하좌우로 이동가능하니까!
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            # is_valid_coord로 맵안에 있는지 여부를 판단
            if is_Valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))
