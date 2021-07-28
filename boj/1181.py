from sys import stdin

N = int(stdin.readline())

array = list()

for i in range(N):
   array.append(stdin.readline())

array.sort(key = lambda x : (len(x) , x ))

# 그냥 set으로 만들면 순서가 지켜지지 않는다.
new_list = []

for i in array:
    if i not in new_list:
        new_list.append(i)

for i in range(len(new_list)):
    print(new_list[i],end='')
