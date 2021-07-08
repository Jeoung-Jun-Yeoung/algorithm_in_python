point = int(input())

if point >= 90:
    print('A')
elif (80 <= point) or (89 <= point):
    print('B')
elif (70 <= point) or (79 <= point):
    print('C')
elif (60 <= point) or (69 <= point):
    print('D')
else:
    print('F')
