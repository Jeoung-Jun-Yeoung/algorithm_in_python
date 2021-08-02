from sys import stdin

n = int(stdin.readline())

sum = 1000 - n
rst = 0

while True:
    if sum == 0:
        print(rst)
        break
    if sum >= 500:
        rst += sum//500
        sum = sum%500
        continue
    elif sum >=100:
        rst += sum//100
        sum = sum%100
        continue
    elif sum >=50:
        rst += sum//50
        sum = sum%50
        continue
    elif sum >=10:
        rst += sum//10
        sum = sum%10
        continue
    elif sum >=5:
        rst += sum//5
        sum = sum%5
        continue
    elif sum >=1:
        rst += sum//1
        sum = sum - sum