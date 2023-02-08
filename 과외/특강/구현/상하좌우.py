N = int(input())

board = [[0] * N for _ in range(N)]

diry = (0, 0, 1, -1)  # 행 가로
dirx = (1, -1, 0, 0)  # 열 세로

# 0 : 오른쪽
# 1 : 왼쪽
# 2 : 남쪽
# 3 : 북쪽


def is_valid_board(x, y, n):
    return (0 < x < n) and (0 < y < n)


movePlan = list(input().split())
# 시작좌표 (0,0)
print(board)
print(movePlan)
x = 1
y = 1
for dir in movePlan:
    dx = 0
    dy = 0
    if dir == 'R':
        dy = y + diry[0]
        dx = x + dirx[0]
        if is_valid_board(dy, dx, N):
            y = dy
            x = dx
    elif dir == 'L':
        dy = y + diry[1]
        dx = x + dirx[1]
        if is_valid_board(dy, dx, N):
            y = dy
            x = dx
    elif dir == 'D':
        dy = y + diry[2]
        dx = x + dirx[2]
        if is_valid_board(dy, dx, N):
            y = dy
            x = dx
    elif dir == 'U':
        dy = y + diry[3]
        dx = x + dirx[3]
        if is_valid_board(dy, dx, N):
            y = dy
            x = dx
    print(f'Y {y} X {x} dir {dir}')
print(f'y {y} x {x} ')
