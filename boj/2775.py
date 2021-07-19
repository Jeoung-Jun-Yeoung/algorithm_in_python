n = int(input())

# y, x = 10, 5
arr = []
#before_room = 0

for i in range(n): # i is test count
    arr = [[0 for _ in range(15)] for _ in range(15)]
    arr[0] = [i for i in range(15)]
    floor = int(input())
    room_num = int(input())
    for k in range(1,floor + 1):
        for j in range(room_num + 1): # j is a count in froom number at the floor 
            arr[k][j] = arr[k][j - 1] + arr[k - 1][j]
    print(arr[floor][room_num])
    