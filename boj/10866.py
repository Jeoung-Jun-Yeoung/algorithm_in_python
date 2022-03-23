# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.


import sys


N = int(sys.stdin.readline())
dequq = []


def push_front(x):
    dequq.insert(0, x)
    return


def push_back(x):
    dequq.append(x)
    return


def pop_front():
    if dequq:
        temp = dequq.pop(0)
        print(temp)
    else:
        print(-1)
    return


def pop_back():
    # empty인 경우 false를 리턴.
    if dequq:
        temp = dequq.pop()
        print(temp)
    else:
        print(-1)
    return


def size():
    print(len(dequq))
    return


def empty():
    if dequq:
        print(0)
    else:
        print(1)
    return


def front():
    if dequq:
        print(dequq[0])
    else:
        print(-1)
    return


def back():
    if dequq:
        print(dequq[-1])
    else:
        print(-1)
    return


while N != 0:
    order = sys.stdin.readline()[:-1]
    if order.find(" ") != -1:
        order, x = order.split()
        num = int(x)
    if order == "push_front":
        push_front(num)
    elif order == "push_back":
        push_back(num)
    elif order == "pop_front":
        pop_front()
    elif order == "pop_back":
        pop_back()
    elif order == "size":
        size()
    elif order == "empty":
        empty()
    elif order == "front":
        front()
    elif order == "back":
        back()
    else:
        print("comand is not define this deque")

    N = N - 1
