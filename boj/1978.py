import sys


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ck = 0
prime = False
for i in nums:
    if i != 1:
        prime = is_prime(i)
    if prime:
        ck = ck + 1

print(ck)
