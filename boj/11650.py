dic = {}

N = int(input())
arrx = list()
arry = list()
for i in range(N):
    x, y = map(int, input().split())
    arrx.append(x)
    arry.append(y)

for cur in range(0, N):  # 01234
    for next in range(1, N - 1):  # 123
        print()
        print(arrx[cur], arrx[next])
        print(arry[cur], arry[next])
        # if(arrx[next] < arrx[cur]):
        #     tempx = arrx[cur]
        #     arrx[cur] = arrx[next]
        #     arrx[next] = tempx
        #     tempy = arry[cur]
        #     arry[cur] = arry[next]
        #     arry[next] = tempy
        # if(arrx[next] == arrx[cur] and arry[next] < arry[cur]):
        #     tempx = arrx[cur]
        #     arrx[cur] = arrx[next]
        #     arrx[next] = tempx
        #     tempy = arry[cur]
        #     arry[cur] = arry[next]
        #     arry[next] = tempy


#print(arrx, arry)
