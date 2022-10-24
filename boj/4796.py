case = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break

    cnt = (V // P) * L
    if V % P < L:
        cnt += V % P

    else:
        cnt += L

    print(f"Case {case}: {cnt}")
    case += 1
