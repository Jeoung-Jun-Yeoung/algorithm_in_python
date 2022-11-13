T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _ = input()
    temp = list(map(int, input().split()))
    temp.sort()
    print(f"#{test_case} ", end="")

    for idx in range(len(temp)):
        if idx == len(temp) - 1:
            print(temp[idx], end="")
            break
        print(temp[idx], end=" ")
    print()
    # print(f"{test_case}" temp)
