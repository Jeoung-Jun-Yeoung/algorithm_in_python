from collections import deque

dy = (0, 1, 0, -1)

dx = (1, 0, -1, 0)


def is_valid_coord(y, x, N, M):
    return 0 <= y < N and 0 <= x < M


def solution():
    answer = 0
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
        1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

    def bfs(maps):
        N = len(maps)
        M = len(maps[0])

        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True

        q = deque()
        q.append((0, 0, 0))

        while q:
            y, x, d = q.popleft()

            if y == N - 1 and x == M - 1:
                return d

            nd = d + 1

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if is_valid_coord(ny, nx, N, M) and maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, nd))

    ans = bfs(maps)

    print(ans)


solution()
