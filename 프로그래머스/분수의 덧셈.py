def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def solution(denum1, num1, denum2, num2):
    answer = []

    numRst = num1 * num2

    denumRst = (denum1 * num2) + (denum2 * num1)

    print(numRst)
    print(denumRst)
    temp = gcd(numRst, denumRst)
    print(
        f"temp : {temp}, numRst {numRst // temp} , denumRst {denumRst // temp}")
    answer.append(denumRst // temp)
    answer.append(numRst // temp)

    return answer
