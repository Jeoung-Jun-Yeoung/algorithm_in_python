from itertools import count
import sys

input = sys.stdin.readline

TodayBook = list()
CountBook = list()
SettleBook = list()


for _ in range(int(input())):
    BookName = input()
    if BookName not in CountBook:
        CountBook.append(BookName)
    TodayBook.append(BookName)

max = 0

for name in CountBook:
    cnt = 0
    for i in range(len(TodayBook)):
        if TodayBook[i] == name:
            cnt = cnt + 1
    SettleBook.append((name, cnt))
    if max <= cnt:
        max = cnt

SettleBook.sort()

while SettleBook:
    rst = SettleBook.pop(0)
    if max == rst[1]:
        print(rst[0])
        break
