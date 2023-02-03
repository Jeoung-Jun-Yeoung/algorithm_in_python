from itertools import permutations


# def searchPermutations(origin, case, n):
#     ps = list(permutations(case, len(case)))

#     if len(ps) < n:
#         print(f"{origin} {n} = No permutation")
#         return
#     n = n - 1
#     # n값 조정
#     for index, value in enumerate(ps):
#         if index == n:
#             rst = "".join(value)
#             print(f"{origin} {n + 1} = {''.join(value)}")
#             return


while True:
    try:
        origin, N = input().split()
        N = int(N)
        testCase = list(origin)
        ps = list(permutations(testCase, len(testCase)))
        if len(ps) < N:
            print(f"{origin} {N} = No permutation")
            continue
        N = N - 1
        # n값 조정
        for index, value in enumerate(ps):
            if index == N:
                rst = "".join(value)
                print(f"{origin} {N + 1} = {''.join(value)}")

    except EOFError:
        break
