# 파이썬의 람다에 대해 공부해 보았습니다.


'''
def add(x,y):
    return x + y

다음과 같은 함수를 람다로 표현할 수 있습니다.

(lanmbda x,y: x + y)(10,20)

map(lambda x: x ** 2, range(5))             # 파이썬 2
[0, 1, 4, 9, 16]
list(map(lambda x: x ** 2, range(5)))     # 파이썬 2 및 파이썬 3
[0, 1, 4, 9, 16]

'''
print(list(map(lambda x: x ** 2, range(5))))
