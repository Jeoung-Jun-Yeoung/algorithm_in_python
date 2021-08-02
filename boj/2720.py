from sys import stdin

t = int(stdin.readline())

for i in range(t):
    q = 0
    n = 0
    d = 0
    p = 0
    input = int(stdin.readline())
    q = input//25
    if input%25 != 0:
        input = input%25
        d = input//10
        if input%10 != 0:
            input = input%10
            n = input//5
            if input%5 != 0:
                input = input%5
                p = input//1
    print(q,d,n,p)
