from collections import deque

n, m = map(int, input().split())

graph = []

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


def is_valid_graph(x, y):

    return (0 <= x < n) and (0 <= y < m)


for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y, graph):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    q = deque()
    q.append([cnt, x, y])
    visited[x][y] = True

    while q:
        cnt, x, y = q.popleft()
        cnt += 1
        if x == (n - 1) and y == (m - 1):
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_valid_graph(nx, ny):
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([cnt, nx, ny])

    # 1이면서 안가봣으면 가면 됨. 0이면 못감


print(bfs(0, 0, graph))
# 0은 못감. 1은 갈수 있음 N,M이면 탈출
