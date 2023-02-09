from collections import deque

n, m = map(int, input().split())

graph = []

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


def is_valid_graph(x, y):
    return 0 <= x < n and 0 <= y < m


for _ in range(n):
    graph.append(list(map(int, input())))
print(graph)


def bfs(x, y, graph):
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    q = deque()
    q.append([cnt, x, y])
    visited[x][y] = True

    while q:
        cnt, x, y = q.popleft()
        if x == n and y == m:
            return cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(f'nx {nx} ny {ny}')
            if not visited[nx][ny] and graph[nx][ny] == 1 and is_valid_graph(nx, ny):
                visited[nx][ny] = True
                q.append([cnt, nx, ny])

    # 1이면서 안가봣으면 가면 됨. 0이면 못감


n -= 1
m -= 1
print(bfs(0, 0, graph))
# 0은 못감. 1은 갈수 있음 N,M이면 탈출
