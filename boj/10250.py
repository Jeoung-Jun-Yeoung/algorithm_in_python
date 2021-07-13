n = int(input())

for _ in range(0,n):
    h,w,o = map(int,input().split())

    if o%h == 0:
        y = h
        x = (o//h) 
    else:
        y = o%h
        x = (o//h) + 1
    
    if x < 10:
        anw = "0"
        anw = anw + str(x)
        print(str(y)+anw)
    else:
        print(str(y)+str(x))