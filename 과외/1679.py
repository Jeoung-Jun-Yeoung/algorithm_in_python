from collections import deque

# 숨바꼭질
# 실버1


def walkPlus(subin):
    return subin + 1


def walkMin(subin):
    return subin - 1


def jump(subin):
    return subin * 2


def excution(nowSubin, subinSister):
    wP = abs(subinSister - walkPlus(nowSubin))
    wM = abs(subinSister - walkMin(nowSubin))
    jp = abs(subinSister - jump(nowSubin))
    # print(f'what is min {min(wP,wM,jp)}')
    if min(wP, wM, jp) == jp:
        return jump(nowSubin)
    elif min(wP, wM, jp) == wP:
        return walkPlus(nowSubin)
    elif min(wP, wM, jp) == wM:
        return walkMin(nowSubin)


def bfs(subin, subinSister):
    # 3개의 값을 다 넣어줘야 겠다.

    q = deque()
    jp = jump(subin)
    wp = walkPlus(subin)
    wm = walkMin(subin)
    count = 1

    if subinSister in [jp, wp, wm]:
        return count

    q.append([count, jp, wp, wm])
    # https://programmers-story.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-deque-TypeError-cannot-unpack-non-iterable-int-object
    #  선언과 하면 오류남..
    # 일단 처음에는 다 넣어줌

    while q:
        count, nowSubinJump, nowSubinP, nowSubinM = q.popleft()
        print(f'count {count} nJ {nowSubinJump} nP {nowSubinP} nM {nowSubinM}')
        ck = [nowSubinJump, nowSubinP, nowSubinM]

        if subinSister in ck:
            return count

        count += 1

        for temp in ck:
            q.append([count, jump(temp), walkPlus(temp), walkMin(temp)])


subin, subinSister = map(int, input().split())

count = bfs(subin, subinSister)
print(count)
