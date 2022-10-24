from collections import deque

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)


def is_valid_coord(y, x, N, M):
    return 0 <= y < N and 0 <= x < N


def bfs():
    chk = [[False] * M for _ in range(N)]

    chk[0][0] = True

    dq = deque()
    dq.append((y, x, 1))

    while dq:
        y, x, d = dq.popleft()
        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == "1" and not visited[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))
