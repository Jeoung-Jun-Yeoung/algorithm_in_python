N = int(input())
target = int(input())
map = [[0 for _ in range(N)] for i in range(N)]

# for i in range(N):
#     print(map[i][0])

# 0 ~ 4 이동에 따른 값 조정을 하면 된다?

# map[][] 내려감 0번째 조절
# map[][] right 이동 1번째 조절
# map[][] 올라감 0번째 조절
# map[][] left 이동 1번째 조절


# 방향과 갱신여부만 체크한다.

# 0 ~ N - 1
# X >= N

# 내 현재위치가 아니라 앞으로 갈 위치가 올바른지 판단해야 맞음
# 원래는 앞으로 갈 위치를 판단해야함.
def is_valid_map(col, row, map):
    # 여기서 방향에 따라서 확인하는게 더 나을수도 있었음
    if col < 0 or col >= N or row >= N or row < 0:
        return False
    # 좌포가 범위내에 있는지는 확인.

    # map안에 정상적으로 있다는건데.
    if map[col][row] == 0:
        return True
        # 갱신을 안한거.
    else:
        return False
    #  갱신한거

# map 안에서 움직이면되는데 첫번째는 [left][right] -> left를 바꿔가며 시작


val = N * N
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 0 1 2
dir = (0, 1, 2, 3)
# 아래 오 위 왼
dir2 = dir[0]
# 내려가는거 시작
row = 0
col = 0

while val > 0:  # <- 바꾸면서
    # 한방향내에서 전진하면서 갱신 for문이 아래로 하면 됌.
    # print(f"col {col} row {row} val {val} map {map}")
    if is_valid_map(col, row, map):
        map[col][row] = val
        # 방향에 따라 판단해서 col or row값을 조절한다.
        if dir2 == 0:
            col += 1
        elif dir2 == 1:
            row += 1
        elif dir2 == 2:
            col -= 1
        elif dir2 == 3:
            row -= 1
        val -= 1
    else:
        # print("ck")
        # col = 3, row = 0 인상황 에서 오른쪽으로 바꿔야함.
        if dir2 == 0:
            dir2 = 1
            # 오른쪽으로 바꿔주고, col을 원래대로 바꿔줌.
            col -= 1
            row += 1
            continue
        elif dir2 == 1:
            dir2 = 2
            row -= 1
            col -= 1
            continue
        elif dir2 == 2:
            dir2 = 3
            col += 1
            row -= 1
            continue
        elif dir2 == 3:
            dir2 = 0
            row += 1
            col += 1
            continue

for i in range(N):
    print(*map[i])

for i in range(N):
    for j in range(N):
        if map[i][j] == target:
            print(i + 1, j + 1)
