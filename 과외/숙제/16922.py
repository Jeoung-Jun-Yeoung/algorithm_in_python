from itertools import combinations_with_replacement
from itertools import combinations

N = int(input())

# romanNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
romanNum = [1, 5, 10, 50]
# 어떤 기호로 생각했다. 숫자든 문자든 상관없지 않은가?
output = []
# print(f'range {range(4)}')
for temp in combinations_with_replacement(range(4), N):
    print(f"temp {temp}")
    sum = 0
    for i in temp:
        print(f"i {i}")
        sum += romanNum[i]
    print(f'sum {sum}')
    output.append(sum)
output.sort()
print(output, len(output))
print()
print()
print(set(output), len(set(output)))

# 아이디어 IIIIIL과 VXXXXX는 문자 표현은 다르지만 값은 55로 같다.. 이런 문제가 발생하기 시작함
# 그래서 조합을 뽑았으면 값을 계산해서 넣어준다. 우리의 목표는 서로 다른 수의 개수를 구하는 것이다.
# 이후 IIIIIL로 55던 VXXXXX로 55던 어차피 같은 55니까 중복을 제거해줘야 한다. 만약 내가 처음 접근한 로직이면,,
# IIIIIL과 VXXXX는 서로 다른 문자의 조합으로 뽑은거니까 중복제거가 안됨
