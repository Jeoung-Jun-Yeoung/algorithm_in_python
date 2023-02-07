# 어떤 수 N이 1이 될때 까지 다음의 두 과정중 하나를 반복적으로 선택하여 수행
# 단 두번째 연산은 N이 K로 나누어 떨어질대만 선택 가능

N, K = map(int, input().split())


count = 0
while N >= K:  # 더이상 나눌 수 없을때까지 한다.
    if (N % K) == 0:
        # 나누어 떨어지는 경우
        if (N // K) < (N - 1):
            N = N // K
            count += 1
    else:
        N = N - 1
        count += 1

while N > 1:
    N -= 1
    count += 1
print(count)
