from sys import stdin

n = int(stdin.readline())
s = set()
for i in range(n):
    read = stdin.readline()[:-1]
    
    if read == "all":
        s = {i for i in range(1,21)}
    elif read == "empty":
        s = set()
    else:
        c,temp = read.split()
        num = int(temp)
        if c == "add":
            s.add(num)
        elif c == "remove":
            s.discard(num)
        elif c == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif c == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)