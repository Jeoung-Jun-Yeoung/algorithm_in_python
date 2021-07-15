n = int(input())

arr = []
#before_room = 0

for i in range(15):
    line = []
    for j in range(15):
        line.append(0)
    arr.append(line)
# and or 
for i in range(n): # i is test count
    floor = int(input())
    room_num = int(input())
    for k in range(floor + 1):
        #print('k',k)
        for j in range(room_num + 1): # j is a count in froom number at the floor 
            #print('j',j)
            if(k == 0): 
                arr[k][j] = j
            else: 
                for m in range(1,j + 1):
                    #before_room += arr[k-1][m - 1]
                    arr[k][j] += arr[k-1][m]
    print(arr[floor][room_num])
    arr = [[0]*15 for _ in range(15)]