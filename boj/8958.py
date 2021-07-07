n = int(input())
for i in range(0,n):
    str = input()
    count = 0
    rst = 0
    for j in str:
        if j == 'O':
            count += 1
            rst += count
        elif j == 'X':
            count = 0
    
    print(rst)