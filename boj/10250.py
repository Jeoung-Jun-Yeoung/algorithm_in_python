n = int(input())

for _ in range(0,n):
    h,w,o = map(int,input().split())

    y = o%h
    x = (o//h) + 1
    
    if x < 10:
        anw = "0"
        anw = anw + str(x)
        
    print(str(y)+anw)
