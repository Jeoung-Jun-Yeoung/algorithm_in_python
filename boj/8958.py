n = int(input())
count = 0
rst = 0

for i in range(0,n):
    str = list(input())
    
    if(str[i] == 'O'):
        count += 1
        print(count)
    elif(str[i] == 'X'):
        rst += count + 1
        count = 0
        