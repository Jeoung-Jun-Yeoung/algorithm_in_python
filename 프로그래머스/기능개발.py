from collections import deque


def solution(progresses, speeds):
    answer = []

    # 큐에 모든 기능들을 넣어준다.
    queue = deque(progresses)

    # 큐가 빌때까지 반복
    count = 0
    while queue:
        # 진행률을 더해줌.
        for i in range(len(queue)):
            queue[i] += speeds[i]
        print(f"queue {queue}")

        if queue[0] >= 100:
            # queue에 기능개발이 완료된게 최소 1개 이상!
            while True:
                idx = 0
                if not queue:
                    break
                temp = queue.popleft()
                if temp < 100:
                    queue.appendleft(temp)
                    break
                print(f"temp {temp} idx {idx} len {len(queue)}")
                speeds.pop(idx)
                # 여기서 팝을 하면 speeds애들은 정렬이 된다.. 즉 2개중에 0을 제거했으면
                # 앞에놈이 다시 0번 인덱스가됨. 그래서 1로 줄이려하면안됌..
                print(f"speeds {speeds}")
                idx += 1
                count += 1

            if count != 0:
                answer.append(count)
                count = 0

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 진짜 배울게 많다..
# 인덱스 오류가 많이 나는데 젤 많이 하는 실수..
