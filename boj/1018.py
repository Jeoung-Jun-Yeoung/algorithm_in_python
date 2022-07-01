n, m = map(int, input().split())

matrix = [input() for _ in range(n)]

# print(matrix)

white_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

black_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]


def check(i, j):
    result_white = 0
    result_black = 0

    for di in range(8):
        for dj in range(8):
            ni, nj = i + di, j + dj
            if matrix[ni][nj] != white_board[di][dj]:
                result_white += 1
            if matrix[ni][nj] != black_board[di][dj]:
                result_black += 1
    return min(result_black, result_white)


result = 1000

for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, check(i, j))

print(result)
