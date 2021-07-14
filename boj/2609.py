a,b = map(int,input().split())

def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    while b!= 0:
        n = a%b
        a = b
        b = n
    return a

rstgcd = gcd(a,b)
rstlcm = a*b//rstgcd
print(rstgcd)
print(rstlcm)