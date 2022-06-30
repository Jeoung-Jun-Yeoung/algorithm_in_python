import math
import sys
import math

num = str(math.factorial(int(sys.stdin.readline())))

num = num[::-1]

ck = 0
for i in num:
    if i != '0':
        break
    ck = ck + 1
print(ck)
