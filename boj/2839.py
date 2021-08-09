from sys import stdin

n = int(stdin.readline())

a = n%5
b = n//5

while True:
    if a%3 == 0:
        c = a//3
        print(b + c)
        break
    else:
        if b == 0:
            print(-1)
            break
        else:
            b -= 1
            a = a + 5
    
