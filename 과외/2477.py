n = int(input())
dic1 = {}
dic2 = {}
field = []

for _ in range(6):
    dir, val = map(int, input().split())
    # print(f"dir {dir} val {val}")
    if dir not in dic1:
        dic1[dir] = val
    else:
        dic2[dir] = val

# 여기서 가장 긴 값의 방향을 찾는다. 방향에 따라 빼줘야 하는 것도 찾는다.
# 틀리고 깨달은 점. 순서도 중요함.
# 딕셔너리에 넣을때 순서를 고려해서 넣어야 할듯 하다.


# def searchMaxDir(field):
#     field.sort(key=lambda x: x[0])
#     field.reverse()
#     # max(field)를 하면 가장 길이가 긴 둘레의 값, 순서, 방향을 알 수 있음
#     return field


# field = searchMaxDir(field)
# print(field)
# # 여기서부터는 아까 로직의 순서에 따라서 값을 찾아 줘야 한다.
# # 동 1 서 2 남 3 북 4
# print(max(field)[1])

# # 순서는 최대 5차이거나 1차이면 됌.
# if max(field)[1] == 2:
#     # 서쪽인경우
#     temp = max(field)[2]
#     part2 = 1
#     for val, dir, i in field:
#         if dir == 3 and abs(temp - i) == 1 or abs(temp - i) == 5:
#             part1 = max(field)[1] * val
#         if dir == 3 and abs(temp - i) != 1 and abs(temp - i) != 5:
#             part2 *= val
