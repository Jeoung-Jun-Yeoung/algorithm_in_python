n = int(input())
dic = {}
field = []

for i in range(6):
    dir, val = map(int, input().split())
    field.append((val, dir, i))


# 여기서 가장 긴 값의 방향을 찾는다. 방향에 따라 빼줘야 하는 것도 찾는다.

# 틀리고 깨달은 점. 순서도 중요함.
# 딕셔너리에 넣을때 순서를 고려해서 넣어야 할듯 하다.


def searchMaxDir(field):
    field.sort(key=lambda x: x[0])
    field.reverse()
    # max(field)를 하면 가장 길이가 긴 둘레의 값, 순서, 방향을 알 수 있음
    return field


field = searchMaxDir(field)
# print(field)
# 여기서부터는 아까 로직의 순서에 따라서 값을 찾아 줘야 한다.
# 동 1 서 2 남 3 북 4
print(max(field)[0])

# 순서는 최대 5차이거나 1차이면 됌.
# 서쪽인경우
temp = max(field)[2]
temp2 = 0
# 몇번째인지 알수있음
part1 = 0
part2 = 0
testThan = 0
if max(field)[1] == 2:
    # 가장긴게 서쪽
    for val, dir, i in field:
        if dir == 3 and abs(temp - i) == 1 or abs(temp - i) == 5:
            # 차이가 1이거나 5면 바로 옆이라는거임.
            testThan1 = val
            part1 = max(field)[0] * val
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == 3 and abs(temp - i) != 1 and abs(temp - i) != 5:
            part2 = val
            # print(f'part2 dir {dir} val {val} i {i} part2 {part2}')
        if dir == 4:
            temp2 = i
    # print(f'temp2 {temp2}')
    for val, dir, i in field:
        if dir == 1 and abs(temp2 - i) == 1 or abs(temp2 - i) == 5:
            part2 *= val
            # print(f'part2 search dir {dir} val {val} i {i} part2 {part2}')

elif max(field)[1] == 3:
    # 가장긴게 남쪽
    for val, dir, i in field:
        if dir == 1 and abs(temp - i) == 1 or abs(temp - i) == 5:
            # 차이가 1이거나 5면 바로 옆이라는거임.
            part1 = max(field)[0] * val
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == 1 and abs(temp - i) != 1 and abs(temp - i) != 5:
            part2 = val
            # print(f'part2 dir {dir} val {val} i {i} part2 {part2}')
        if dir == 2:
            temp2 = i
    # print(f'temp2 {temp2}')
    for val, dir, i in field:
        if dir == 4 and abs(temp2 - i) == 1 or abs(temp2 - i) == 5:
            part2 *= val
            # print(f'part2 search dir {dir} val {val} i {i} part2 {part2}')

elif max(field)[1] == 4:
    # 가장긴게 북쪽
    for val, dir, i in field:
        if dir == 2 and abs(temp - i) == 1 or abs(temp - i) == 5:
            # 차이가 1이거나 5면 바로 옆이라는거임.
            part1 = max(field)[0] * val
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == 2 and abs(temp - i) != 1 and abs(temp - i) != 5:
            part2 = val
            # print(f'part2 dir {dir} val {val} i {i} part2 {part2}')
        if dir == 1:
            temp2 = i
    # print(f'temp2 {temp2}')
    for val, dir, i in field:
        if dir == 3 and abs(temp2 - i) == 1 or abs(temp2 - i) == 5:
            part2 *= val
            # print(f'part2 search dir {dir} val {val} i {i} part2 {part2}')
else:
    # 가장긴게 동쪽
    for val, dir, i in field:
        if dir == 4 and abs(temp - i) == 1 or abs(temp - i) == 5:
            # 차이가 1이거나 5면 바로 옆이라는거임.
            part1 = max(field)[0] * val
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == 4 and abs(temp - i) != 1 and abs(temp - i) != 5:
            part2 = val
            # print(f'part2 dir {dir} val {val} i {i} part2 {part2}')
        if dir == 3:
            temp2 = i
    # print(f'temp2 {temp2}')
    for val, dir, i in field:
        if dir == 2 and abs(temp2 - i) == 1 or abs(temp2 - i) == 5:
            part2 *= val
            # print(f'part2 search dir {dir} val {val} i {i} part2 {part2}')
print((part1+part2) * n)
