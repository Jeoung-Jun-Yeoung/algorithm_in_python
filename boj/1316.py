from sys import stdin

n = int(stdin.readline())
voca_list = []
rst = n
for i in range(n):
    ck_arr = []
    voca = list(stdin.readline()[:-1])
    for j in range(len(voca)):
        if len(voca) == 1:
            break
        if voca[j] not in ck_arr:
            ck_arr.append(voca[j])
        elif voca[j] in ck_arr:
            if voca[j] != voca[j - 1]:
                rst -= 1
                break
print(rst)