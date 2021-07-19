n = int(input())
anw = 0
for _ in range(0,n):
    h,w,o = map(int,input().split())

    if o%h == 0:
        y = h
        x = (o//h) 
    else:
        y = o%h
        x = (o//h) + 1
    anw = (y * 100) + x
    print(anw)