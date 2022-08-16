import sys

input = sys.stdin.readline

N = int(input())

budget = list(map(int, input().split()))

budget.sort()
total = int(input())

if(sum(budget) <= total):
    print(max(budget))


print(min(budget))
before_mid = 0
mid = total
while mid >= min(budget):
    before_mid = mid
    mid = mid // 2

index = len(budget) / 2
while before_mid >= budget(index):
