
n, m = map(int, input().split())

dic = dict()

for _ in range(n):
    site, pw = map(str, input().split())
    if site not in dic:
        dic[site] = pw

for _ in range(m):
    print(dic[input()])
