n = int(input())
dic = {}
field = []
# 동 1 서 2 남 3 북 4

east = 1
west = 2
south = 3
north = 4

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

# print(max(field)[0])

# 순서는 최대 5차이거나 1차이면 됌.
# 서쪽인경우
temp = max(field)[2]
temp2 = 0
# 몇번째인지 알수있음
part1 = 0
part2 = 1

if max(field)[1] == west:
    # 가장긴게 서쪽
    S = 0
    N = 0
    Si =
    Ni = 0
    # 이때 옆에 있는 북쪽과 남쪽 둘레를 찾는다.
    for val, dir, i in field:
        if dir == south and (abs(temp - i) == 1 or abs(temp - i) == 5):
            # 차이가 1이거나 5면 바로 옆이라는거임.
            S = val
            Si = i
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == north and (abs(temp - i) == 1 or abs(temp - i) == 5):
            N = val
            Ni = i

    if S > N:
        part1 = max(field)[0] * N
        # 남쪽이 더 긴상황. 선생님이 알려준 상황.
        for val, dir, i in field:
            if dir == north and Ni != i:
                part2 *= val
            if dir == east and (abs(Si - i) == 1 or abs(Si - i) == 5):
                part2 *= val
    else:
        # 북쪽이 더 긴상황. 아까처럼 일반적인 경우
        part1 = max(field)[0] * S
        for val, dir, i in field:
            if dir == south and i != Si:
                part2 *= val
            if dir == east and (abs(Ni - i) == 1 or abs(Ni - i) == 5):
                part2 *= val
elif max(field)[1] == north:
    # 가장긴게 북쪽
    W = 0
    E = 0
    Wi = 0
    Ei = 0
    # 이때 옆에 있는 서쪽과 동쪽 둘레를 찾는다.
    for val, dir, i in field:
        # print(f'val {val} , dir {dir}, i {i}')
        if dir == west and (abs(temp - i) == 1 or abs(temp - i) == 5):
            # 차이가 1이거나 5면 바로 옆이라는거임.
            W = val
            Wi = i
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == east and (abs(temp - i) == 1 or abs(temp - i) == 5):
            E = val
            Ei = i
    if W > E:
        part1 = max(field)[0] * E
        # 서쪽이 더 긴상황. 선생님이 알려준 상황.
        for val, dir, i in field:
            if dir == east and Ei != i:
                part2 *= val
            if dir == south and (abs(Wi - i) == 1 or abs(Wi - i) == 5):
                part2 *= val
    else:
        # 동쪽이 더 긴상황. 아까처럼 일반적인 경우
        part1 = max(field)[0] * W
        for val, dir, i in field:
            if dir == west and i != Wi:
                part2 *= val
            if dir == south and (abs(Ei - i) == 1 or abs(Ei - i) == 5):
                part2 *= val
elif max(field)[1] == east:
    # 가장긴게 동쪽
    N = 0
    S = 0
    Ni = 0
    Si = 0
    # 이때 옆에 있는 북쪽과 남쪽 둘레를 찾는다.
    for val, dir, i in field:
        if dir == south and (abs(temp - i) == 1 or abs(temp - i) == 5):
            # 차이가 1이거나 5면 바로 옆이라는거임.
            S = val
            Si = i
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == north and (abs(temp - i) == 1 or abs(temp - i) == 5):
            N = val
            Ni = i

    if N > S:
        part1 = max(field)[0] * S
        # 서쪽이 더 긴상황. 선생님이 알려준 상황.
        for val, dir, i in field:
            if dir == south and Si != i:
                part2 *= val
            if dir == west and (abs(Ni - i) == 1 or abs(Ni - i) == 5):
                part2 *= val
    else:
        # 동쪽이 더 긴상황. 아까처럼 일반적인 경우
        part1 = max(field)[0] * N
        for val, dir, i in field:
            if dir == north and i != Ni:
                part2 *= val
            if dir == west and (abs(Si - i) == 1 or abs(Si - i) == 5):
                part2 *= val
elif max(field)[1] == south:
    # 가장긴게 남쪽
    W = 0
    E = 0
    Wi = 0
    Ei = 0
    # 이때 옆에 있는 북쪽과 남쪽 둘레를 찾는다.
    for val, dir, i in field:
        if dir == west and (abs(temp - i) == 1 or abs(temp - i) == 5):
            # 차이가 1이거나 5면 바로 옆이라는거임.
            W = val
            Wi = i
            # print(f'part1 dir {dir} val {val} i {i} part1 {part1}')
        if dir == east and (abs(temp - i) == 1 or abs(temp - i) == 5):
            E = val
            Ei = i
    if W > E:
        part1 = max(field)[0] * E
        # 서쪽이 더 긴상황. 선생님이 알려준 상황.
        for val, dir, i in field:
            if dir == east and Ei != i:
                part2 *= val
            if dir == north and (abs(Wi - i) == 1 or abs(Wi - i) == 5):
                part2 *= val
    else:
        # 동쪽이 더 긴상황. 아까처럼 일반적인 경우
        part1 = max(field)[0] * W
        for val, dir, i in field:
            if dir == west and i != Wi:
                part2 *= val
            if dir == south and (abs(Ei - i) == 1 or abs(Ei - i) == 5):
                part2 *= val

print((part1+part2) * n)
