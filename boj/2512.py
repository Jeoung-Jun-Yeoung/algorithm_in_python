import sys

input = sys.stdin.readline

N = int(input())

budget = list(map(int, input().split()))

budget.sort()
total = int(input())

if(sum(budget) <= total):
    print(max(budget))
else:
    before_mid = 0
    mid = total
    while mid >= min(budget):
        before_mid = mid
        mid = mid // 2

    index = len(budget) // 2

    while before_mid <= budget[index]:
        index = index // 2
    sum = 0
    for i in range(0, index + 1):
        sum += before_mid - budget[i]

    sum = sum // (index + 1)

    before_mid = before_mid + sum

    print(before_mid)
