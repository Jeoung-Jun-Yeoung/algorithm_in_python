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


def is_valid_ran(nowSubin):
    return (0 <= nowSubin) and (nowSubin <= 200000)


def bfs(subin, subinSister):
    # 3개의 값을 다 넣어줘야 겠다.

    q = deque()
    count = 0
    visited = [False] * (200000 + 1)
    q.append([count, subin])
    # https://programmers-story.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-deque-TypeError-cannot-unpack-non-iterable-int-object
    #  선언과 하면 오류남..
    # 일단 처음에는 다 넣어줌
    visited[subin] = True
    while q:
        count, nowSubin = q.popleft()
        # print(f'count {count} nJ {nowSubinJump} nP {nowSubinP} nM {nowSubinM}')

        if subinSister == nowSubin:
            return count

        count += 1
        # for i in range(4):
        # nx = x + dx[i]
        # ny = y + dy[i]
        # for i in graph[now]:

        for maybeSubin in [jump(nowSubin), walkPlus(nowSubin), walkMin(nowSubin)]:
            # 3가지 경우의수를 봐야할거같다.
            # 범위안에 있는지 확인하고,

            if is_valid_ran(maybeSubin) and not visited[maybeSubin]:
                # index 체크를 항상 먼저 오고, 그 다음에 나머지 조건을 체크해준다.
                # short 서킷 and 앞조건이 False이면 뒤에것을 보지 않는다.
                visited[maybeSubin] = True
                q.append([count, maybeSubin])
            # q.append([count, jump(temp), walkPlus(temp), walkMin(temp)])


subin, subinSister = map(int, input().split())

visited = []
count = bfs(subin, subinSister)
print(count)
