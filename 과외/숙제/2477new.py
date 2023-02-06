# 어떤 형태로 들어올지 모르는건 정규화를 해야한다.

# 동 1 : 남 : 3 : 서 : 2 : 북 : 4


# def rotate90(v):
#     return[0, 3, 4, 2, 1][v]


def two_logest(A):
    # 동or서 and 남or북에서 긴걸 찾는다.
    even = max([0, 2, 4], key=lambda x: A[x])
    odd = max([1, 3, 5], key=lambda x: A[x])
    return even, odd


def main():
    k = int(input())
    A = []
    for i in range(6):
        dir, val = map(int, input().split())
        A.append((val, dir))

    while two_logest(A) != (0, 1):
        print(f'before A {A}')
        A = A[1:] + A[:1]
        print(f'afeter A {A}')
    print(k * (A[0][0] * A[1][0] - A[3][0] * A[4][0]))


if __name__ == '__main__':
    main()
