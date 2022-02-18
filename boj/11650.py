dic = {}

N = int(input())
arrx = list()
arry = list()
for i in range(N):
    x, y = map(int, input().split())
    arrx.append(x)
    arry.append(y)

for cur in range(N):  # 01234
    for next in range(1, N - 1):  # 123
        # print()
        # print(arrx[cur], arrx[next])
        # print(arry[cur], arry[next])
        if(arrx[cur] > arrx[next]):
            tempx = arrx[cur]
            arrx[cur] = arrx[next]
            arrx[next] = tempx
            tempy = arry[cur]
            arry[cur] = arry[next]
            arry[next] = tempy
        if(arrx[cur] == arrx[next] and arry[cur] > arry[next]):
            arry[cur] = arry[next]
            arry[next] = tempy

print(arrx, arry)
