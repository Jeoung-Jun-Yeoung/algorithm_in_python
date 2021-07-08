list = list(map(int,input().split()))
rst = 0
for i in range(0,len(list)):
    rst += (list[i] * list[i])

print(rst%10)

