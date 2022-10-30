from collections import deque


def soulution(priorty, location):
    printer = deque()
    printer = [(i, q) for i, q in enumerate(priorty)]

    cnt = 0
    while printer:
        job = printer.popleft()
        if any(job[1] < other_job[1] for other_job in printer):
            printer.append(job)
        else:
            cnt += 1
            if job[0] == location:
                break
    print(cnt)
