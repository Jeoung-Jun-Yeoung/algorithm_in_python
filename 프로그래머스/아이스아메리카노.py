def solution(money):
    answer = []
    iceame = 5500

    answer.append(money // iceame)
    answer.append(money % iceame)
    return answer
