T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    rst = 0
    for num in range(1, int(input()) + 1):
        if num % 2 == 0:
            # 나머지가 0이면 짝수
            rst -= num
        else:
            rst += num
    print(f"#{test_case} {rst}")
