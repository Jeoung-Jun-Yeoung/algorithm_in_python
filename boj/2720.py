from sys import stdin

t = int(stdin.readline())

arr = [25,10,5,1]
for i in range(t):
    rst = []
    input = int(stdin.readline())
    for j in arr:
        rst.append(str(input//j))
        input = input%j
    print(" ".join(rst))

# join 함수
# join 연속으로 들어오는 문자열을 특정 기준으로 만들어준다.
