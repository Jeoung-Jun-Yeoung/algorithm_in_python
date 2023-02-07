stringNum = input()

num = [int(i) for i in stringNum]


num.sort(reverse=True)

rst = 1
for i in num:
    if i == 0:
        rst += 0
    elif i == 1:
        rst += 1
    else:
        rst *= i
    print(f'i {i} rst {rst}')
print(rst)
