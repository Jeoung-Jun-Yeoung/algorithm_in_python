from itertools import permutations

while True:
    try:
        origin, n = input().split()
        temp = int(n)
        flag = False
        for ps in permutations(list(origin), len(list(origin))):
            temp -= 1
            if temp == 0:
                print(f"{origin} {n} = {''.join(list(ps))}")
                flag = True
                break
        if flag:
            continue
        else:
            print(f"{origin} {n} = No permutation")

    except:
        break
