rst = ''
for i in input():
    if i.isupper():
        rst += i.lower()
    else:
        rst += i.upper()
print(rst)
