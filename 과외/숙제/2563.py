n = int(input())

# think 종이는 여러장 일 수 있다.
# 전체 종이가 안곂쳤다면 n * 100이 색종이의 크기.
# 이때 곂치는 부분만 n * 100에서 빼준다
# n * 100 - 곂치는 부분의 길이

overX = []
overY = []

paperX = []
paperY = []

# paperX[[]]
for i in range(n):
    x, y, = map(int, input().split())
    tempX = [x for x in range(x, x+10, 1)]
    tempY = [y for y in range(y, y+10, 1)]

    for ckX in overX:
        for tmpX in tempX:
            if ckX == tmpX:
                # 이미 기존에 곂치는것. 기존에 제거해준거임
                tempX.remove(tmpX)
    for ckY in overY:
        for tmpY in tempY:
            if ckY == tmpY:
                # 이미 기존에 곂치는것. 기존에 제거해준거임
                tempX.remove(tmpY)
    # 곂치는거 제거해줌

    # papaer 길이 확인
