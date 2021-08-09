from sys import stdin

n = int(stdin.readline())

for i in range(n):
    array = input()
    empty_array = list()
    flag = 0
    for j in array:
        if j == '(':
            empty_array.append(j)
        elif j == ')':
            if not empty_array:
                flag = 1
                break
            empty_array.pop()
    if not empty_array and flag != 1:
        print('YES')
    else:
        print('NO')