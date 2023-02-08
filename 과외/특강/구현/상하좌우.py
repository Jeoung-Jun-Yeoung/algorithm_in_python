N = int(input())

board = [[0] * N for _ in range(N)]


def is_valid_board(x, y, n):
    return (x >= 0 and x < n) or (y >= 0 and y < n)


movePlan = list(input().split())

print(board)
print(movePlan)

# +1을 해주자
