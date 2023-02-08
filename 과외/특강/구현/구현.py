dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

x, y = 2, 2


def is_valid_map(x, y, n, m):
    return (0 <= x and x < n) or (y <= 0 and y < m)


for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
