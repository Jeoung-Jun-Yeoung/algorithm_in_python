A = int(input())
B = int(input())
arr_B = [int(i) for i in str(B)]
# print(f"arr_B {arr_B}")
arr_B.reverse()
# print(f"after {arr_B}")
for i in range(len(arr_B)):
    print(A * arr_B[i])
    # print(f"A {A} * arr_B {arr_B[i]} {A * arr_B[i]}")
print(A * B)
