a,b = input().split()

re_a = "".join(reversed(a))
re_b = "".join(reversed(b))


if int(re_a) > int(re_b):
    print(re_a)
else:
    print(re_b)
