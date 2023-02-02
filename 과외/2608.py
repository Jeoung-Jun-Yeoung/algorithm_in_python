# 문제
# 로마 시대 때는 현재 사용하는 아라비아 숫자가 아닌 다른 방법으로 수를 표현하였다.

# 로마 숫자는 다음과 같은 7개의 기호로 이루어진다.

# 기호	I	V	X	L	C	D	M
# 값	1	5	10	50	100	500	1000
# 수를 만드는 규칙은 다음과 같다.

# 보통 큰 숫자를 왼쪽에 작은 숫자를 오른쪽에 쓴다. 그리고 그 값은 모든 숫자의 값을 더한 값이 된다. 예를 들어 LX = 50 + 10 = 60 이 되고, MLI = 1000 + 50 + 1 = 1051 이 된다.
# V, L, D는 한 번만 사용할 수 있고 I, X, C, M은 연속해서 세 번까지만 사용할 수 있다. 예를 들어 VV나 LXIIII 와 같은 수는 없다. 그리고 같은 숫자가 반복되면 그 값은 모든 숫자의 값을 더한 값이 된다. 예를 들어 XXX = 10 + 10 + 10 = 30 이 되고, CCLIII = 100 + 100 + 50 + 1 + 1 + 1 = 253 이 된다.
# 작은 숫자가 큰 숫자의 왼쪽에 오는 경우는 다음과 같다. IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900 을 나타낸다. 이들 각각은 한 번씩만 사용할 수 있다. 그런데 IV 와 IX 는 같이 쓸 수 없으며 XL 과 XC, CD 와 CM 또한 같이 쓸 수 없다. 이들 외에는 작은 숫자가 큰 숫자 왼쪽 어디에도 나올 수 없다. 예를 들어 XCXC 나 CMCD, VX 나 IIX 와 같은 수는 없다. 참고로 LIX = 50 + 9 = 59, CXC = 100 + 90 = 190 이 된다.
# 모든 수는 가능한 가장 적은 개수의 로마 숫자들로 표현해야 한다. 예를 들어 60 은 LX 이지 XLXX 가 아니고, 5 는 V 이지 IVI 가 아니다.
# 아래의 예를 참고 하시오.

# DLIII = 500 + 50 + 3 = 553
# MCMXL = 1000 + 900 + 40 = 1940
# 235 = CCXXXV
# 2493 = MMCDXCIII
# 로마 숫자로 이루어진 두 수를 입력받아 그 둘을 더한 값을 아라비아 숫자와 로마 숫자로 출력하는 프로그램을 작성하시오.

def checkSign(sign):
    # signDict = {
    #     'I': 1,

    # }
    # return signDict.get(sign, False)
    # 요렇게 하면 리팩토링 가능
    if sign == 'I':
        return 1
    elif sign == 'V':
        return 5
    elif sign == 'X':
        return 10
    elif sign == 'L':
        return 50
    elif sign == 'C':
        return 100
    elif sign == 'D':
        return 500
    elif sign == 'M':
        return 1000
    else:
        return False


def check2Num(Number):
    temp = [False, 0]
    if Number == "IV":
        temp = [True, 4]
        return temp
    elif Number == "IX":
        temp = [True, 9]
        return temp
    elif Number == "XL":
        temp = [True, 40]
        return temp
    elif Number == "XC":
        temp = [True, 90]
        return temp
    elif Number == "CD":
        temp = [True, 400]
        return temp
    elif Number == "CM":
        temp = [True, 900]
        return temp
    else:
        return temp


romNum1 = list(input())
romNum2 = list(input())
sum = 0
ckNumber = ''
for num in romNum1:

    ckNumber += num
    test = check2Num(ckNumber)
    # print(f"num {num} chekSign(num) {checkSign(num)} ckNumber {ckNumber}")
    # print(f"test {test}")
    if test[0]:
        sum += test[1]
        # 값을 넣어주고 2글자를 안봐도 된다.
        sum -= checkSign(ckNumber[0])
        ckNumber = ''
    else:
        sum += checkSign(num)
        if len(ckNumber) == 2:
            ckNumber = ckNumber[1]

# print(f"sum {sum}")

ckNumber = ''
for num in romNum2:

    ckNumber += num
    test = check2Num(ckNumber)
    # print(f"num {num} chekSign(num) {checkSign(num)} ckNumber {ckNumber}")
    # print(f"test {test}")
    if test[0]:
        sum += test[1]
        # 값을 넣어주고 2글자를 안봐도 된다.
        sum -= checkSign(ckNumber[0])
        ckNumber = ''
    else:
        sum += checkSign(num)
        if len(ckNumber) == 2:
            ckNumber = ckNumber[1]
# print(f"sum {sum}")

# print(*romNum1)
# print(*romNum2)
# print(sum)

# 가장 큰 수부터 제거해 준다.
# 기호	I	V	X	L	C	D	M
# 값	1	5	10	50	100	500	1000
# I X C M은 연속해서 세번까지 가능 이거로 가장 큰것부터 차례로 빼준다.
# 이후 남은 숫자를 써준다. 이때

dic = {"M": 1000, "D": 500, "C": 100, "L": 50,
       "X": 10, "V": 5, "I": 1, "IX": 9,
       "IV": 4, "XL": 40, "XC": 90, "CD": 400,
       "CM": 900}

romaNumber = ''


def arbia2rom(temp):
    global romaNumber
    if temp - dic["M"] >= 0:
        romaNumber += "M"
        temp = temp - dic["M"]
        # 1000
        return temp
    elif temp - dic["CM"] >= 0:
        romaNumber += "CM"
        temp = temp - dic["CM"]
        # 900
        return temp
    elif temp - dic["D"] >= 0:
        romaNumber += "D"
        temp = temp - dic["D"]
        # 500
        return temp
    elif temp - dic["CD"] >= 0:
        romaNumber += "CD"
        temp = temp - dic["CD"]
        # 400
        return temp
    elif temp - dic["C"] >= 0:
        romaNumber += "C"
        temp = temp - dic["C"]
        # 100
        return temp
    elif temp - dic["XC"] >= 0:
        romaNumber += "XC"
        temp = temp - dic["XC"]
        # 90
        return temp
    elif temp - dic["L"] >= 0:
        romaNumber += "L"
        temp = temp - dic["L"]
        # 50
        return temp
    elif temp - dic["XL"] >= 0:
        romaNumber += "XL"
        temp = temp - dic["XL"]
        # 40
        return temp
    elif temp - dic["X"] >= 0:
        romaNumber += "X"
        temp = temp - dic["X"]
        # 10
        return temp
    elif temp - dic["IX"] >= 0:
        romaNumber += "IX"
        temp = temp - dic["IX"]
        # 9
        return temp
    elif temp - dic["V"] >= 0:
        romaNumber += "V"
        temp = temp - dic["V"]
        # 5
        return temp
    elif temp - dic["IV"] >= 0:
        romaNumber += "IV"
        temp = temp - dic["IV"]
        # 4
        return temp
    elif temp - dic["I"] >= 0:
        romaNumber += "I"
        temp = temp - dic["I"]
        # 1
        return temp


temp = sum
# print(f"temp {temp}")
while temp > 0:
    # print(temp)
    temp = arbia2rom(temp)

print(sum)
print(romaNumber)
