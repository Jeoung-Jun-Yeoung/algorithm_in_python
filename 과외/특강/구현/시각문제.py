# N이 입력되면 00시00분00초부터 N시 59분 59초까지의 모든 시각중 3이 하나라도 포함도는 모든 경우의 수

N = int(input())

threeCk = 0
three = [3, 13, 23, 33, 43, 53]
for tempH in range(0, N+1, 1):
    for tempM in range(0, 60, 1):
        for tempS in range(0, 60, 1):
            if '3' in str(tempH)+str(tempM)+str(tempS):
                threeCk += 1
print(threeCk)
