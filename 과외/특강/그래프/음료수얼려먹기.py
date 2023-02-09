import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = []

# testg = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))


def is_valid_graph(x, y):
    global n
    global m
    return 0 <= x < n and 0 <= y < m


dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


def dfs(x, y):
    if not is_valid_graph(x, y):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1  # visited대신에 값을 넣어줌
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            dfs(nx, ny)
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        # dfs(x + 1, y)
        # dfs(x, y + 1)
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
