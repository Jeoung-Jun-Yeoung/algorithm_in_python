from sys import stdin

h,w = map(int,stdin.readline().split())

arr = [0 for _ in range(h)]
rst_arr = []

for i in range(h):
    rst = ''
    flag = 0
    arr[i] = list(map(str,stdin.readline().split()))
    temp = arr[i][0]
    for j in temp:
        if j == 'c':
            rst = rst + '0'
            rst = rst + ' '
            flag = 1
            count = 1
        elif j != 'c' and flag ==1:
            rst = rst + str(count)
            rst = rst + ' '
            count += 1
        else:
            rst = rst + 'n'
            rst = rst + ' '
    rst_arr.append(rst)
    
for i in range(h):
    temp = rst_arr[i]
    for j in temp:
        if j == ' ':
            print(j,end='')
        elif j == 'n':
            print(-1,end='')
        else:
            print(int(j),end='')
    print()
        