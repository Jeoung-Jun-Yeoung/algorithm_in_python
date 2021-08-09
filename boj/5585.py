from sys import stdin

n = int(stdin.readline())

sum = 1000 - n
rst = 0
arr = [500,100,50,10,5,1]


for i in arr:
    rst += sum//i
    sum = sum%i
print(rst)
    # if sum >= 500:
    #     rst += sum//500
    #     sum = sum%500
    #     continue
    # elif sum >=100:
    #     rst += sum//100
    #     sum = sum%100
    #     continue
    # elif sum >=50:
    #     rst += sum//50
    #     sum = sum%50
    #     continue
    # elif sum >=10:
    #     rst += sum//10
    #     sum = sum%10
    #     continue
    # elif sum >=5:
    #     rst += sum//5
    #     sum = sum%5
    #     continue
    # elif sum >=1:
    #     rst += sum//1
    #     sum = sum - sum