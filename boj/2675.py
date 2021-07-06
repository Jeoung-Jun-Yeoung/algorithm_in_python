cnt = int(input())

arr = list()
 
for i in range(0,cnt):
    repeat,test = input().split()

    repeat = int(repeat)
    
    for j in test:
        print(j * repeat, end='')
    print('')