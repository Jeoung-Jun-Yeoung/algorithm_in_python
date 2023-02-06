n = int(input())
# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수

# N번째 감소하는 수를 출력하라
# 0은 0번째 감소하는 수. 1은 1번째 감소하는 수

downNumList = [
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9
]

for i in downNumList:
    test = i % 10
    # print(f'test {test}')``
    for j in range(10):
        if test > j:
            downNumList.append(i * 10 + j)
# print(downNumList)
if n >= len(downNumList):
    print(-1)
else:
    print(downNumList[n])

# 조건은 뭐가 될 수 있을까?
# 앞자리가 뒷자리보다 커야한다는 조건이 있음. 같아도 안된다. (앞자리수 > 뒷자리수)
# 숫자를 스플릿 해서 문자로 만듬. 각각 분리 한다음에 대소비교를 해준다. 이후 조건 만족시 append하면 된다?
