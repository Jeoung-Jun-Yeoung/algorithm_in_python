def solution(n):
    answer = 0
    cnt = []
    # 먼저 n을 2진수로 변환
    # 1의 개수를 센다
    # 이후 비교를 한다.
    start = n
    # n 값이 필요하긴하다. 나중에 n부터 시작해서 값을 한개씩 늘려가며 탐색해야 하는데 n값을 밑에서 고대로 가져다 쓰면서 소실됌

    while n > 0:
        if n % 2 != 0:
            cnt.append(1)
        n = n // 2
    # n의 1갯수
    n_cnt = cnt.count(1)
    # 이거 찾는거까지는 5분안에 짬.

    # 여기서 먼저 기존 n에 2진수에 1이 몇개있는지 체크

    # 찾을 넘의 1갯수
    next_cnt = 0

    cnt.clear()
    # 기존 배열을 재활용하기로 했다. 디버깅하면서 짠 코드

    rst = 0

    for temp in range(start + 1, 1000000):
        # while문으로 시작하려함. 100000이 너무 큰숫자 같았는데 그냥 for문이 나았다
        rst = temp
        # 여기서도 temp가 답이 될 확률이 있기에 저장해둔다.

        while temp > 0:
            if temp % 2 != 0:
                cnt.append(1)
            temp = temp // 2
        # 계산 로직은 위에와 같다. 만약 이후 1이 같다면!! 정답!!
        next_cnt = cnt.count(1)

        # 그리고 다음 숫자를 위해 cnt를 클리어 해주어야 한다.
        cnt.clear()

        if next_cnt == n_cnt:
            break
        # 정답을 찾았다.
    # 해당 값이 정답이기에 answer에 담아준다.
    answer = rst

    return answer
