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


def search_adj(maxLineDir, field):
    temp = max(field)[2]
    if maxLineDir == west or maxLineDir == east:
        for val, dir, i in field:
            if dir == south and (abs(temp - i) == 1 or abs(temp - i) == 5):
                S = val
                Si = i
            if dir == north and (abs(temp - i) == 1 or abs(temp - i) == 5):
                N = val
                Ni = i
        return S, Si, N, Ni
    elif maxLineDir == north or maxLineDir == south:
        for val, dir, i in field:
            if dir == west and (abs(temp - i) == 1 or abs(temp - i) == 5):
                W = val
                Wi = i
            if dir == east and (abs(temp - i) == 1 or abs(temp - i) == 5):
                E = val
                Ei = i
        return W, Wi, E, Ei


def cal_field(maxLineDir, field, n):
    part1 = 1
    part2 = 1
    if maxLineDir == west:
        S, Si, N, Ni = search_adj(west, field)
        if S > N:
            part1 = max(field)[0] * N
            for val, dir, i in field:
                if dir == east and (abs(Si - i) == 1 or abs(Si - i) == 5):
                    part2 *= val
                if dir == north and i != Ni:
                    part2 *= val
        else:
            part1 = max(field)[0] * S
            for val, dir, i in field:
                if dir == south and i != Si:
                    part2 *= val
                if dir == east and (abs(Ni - i) == 1 or abs(Ni - i) == 5):
                    part2 *= val

    elif maxLineDir == east:
        S, Si, N, Ni = search_adj(east, field)
        if S > N:
            part1 = max(field)[0] * N
            for val, dir, i in field:
                if dir == west and (abs(i - Si) == 1 or abs(i - Si) == 5):
                    part2 *= val
                if dir == north and i != Ni:
                    part2 *= val
        else:
            part1 = max(field)[0] * S
            for val, dir, i in field:
                if dir == west and (abs(i - Ni) == 1 or abs(i - Ni) == 5):
                    part2 *= val
                if dir == south and i != Si:
                    part2 *= val
    elif maxLineDir == north:
        W, Wi, E, Ei = search_adj(north, field)
        if W > E:
            part1 = max(field)[0] * E
            for val, dir, i in field:
                if dir == south and (abs(i - Wi) == 1 or abs(i - Wi) == 5):
                    part2 *= val
                if dir == east and i != Ei:
                    part2 *= val
        else:
            part1 = max(field)[0] * W
            for val, dir, i in field:
                if dir == south and (abs(i - Ei) == 1 or abs(i - Ei) == 5):
                    part2 *= val
                if dir == west and i != Wi:
                    part2 *= val

    elif maxLineDir == south:
        W, Wi, E, Ei = search_adj(south, field)
        if W > E:
            part1 = max(field)[0] * E
            for val, dir, i in field:
                if dir == east and i != Ei:
                    part2 *= val
                if dir == north and (abs(i - Wi) == 1 or abs(i - Wi) == 5):
                    part2 *= val
        else:
            part1 = max(field)[0] * W
            for val, dir, i in field:
                if dir == west and i != Wi:
                    part2 *= val
                if dir == south and (abs(i - Ei) == 1 or abs(i - Ei) == 5):
                    part2 *= val
    print((part1 + part2) * n)


field = searchMaxDir(field)
# print(field)
# 여기서부터는 아까 로직의 순서에 따라서 값을 찾아 줘야 한다.

# print(max(field)[0])
# 순서는 최대 5차이거나 1차이면 됌.
# 서쪽인경우

cal_field(max(field)[1], field, n)
