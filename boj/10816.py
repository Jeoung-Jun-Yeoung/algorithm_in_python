from sys import stdin
from collections import defaultdict
from typing import DefaultDict

N = int(stdin.readline())
array = list(map(int,stdin.readline().split()))

dic = defaultdict(int)

for i in array:
    try: dic[i] += 1
    except: dic[i] = 1
M = int(stdin.readline())
arr2 = list(map(int,stdin.readline().split()))

for i in arr2:
    # value = dic.get(i)
    # if value == None:
    #     print(0, end=' ')
    # else:
    print(dic.get(i), end=' ')
# arr1 을 통해 카운트를 하면서 value로 cnt한 값을 넣어준다.
# # defaultdict 둘다 구현하기.
