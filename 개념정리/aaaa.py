dy = (1, 0, -1, 0, 1, -1, 1, -1)
dx = (0, 1, 0, -1, -1, 1, -1, 1)


def is_valid_coord(y, x, N, M):
    return 0 <= y < N and 0 <= x < M


def solution(board):
    N = len(board)
    M = len(board[0])
    print(f"N {N} M {M}")
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                for k in (8):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if is_valid_coord(ny, nx, N, M):
                        board[ny][nx] = 3
    print(board)

    answer = 0
    return answer

    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 3, 3, 3, 0],
     [0, 3, 1, 3, 0],
     [0, 3, 3, 3, 0]]


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0], [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]

solution(board)
