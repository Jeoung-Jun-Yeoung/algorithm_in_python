import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# n개의 도감목록이 입력
# m개의 문제가 나옴. 문제가 알파벳이면 포켓몬 번호를 말하고,
# 문제가 숫자면 해당 포켓몬 이름을 출력


poketmon = []
for _ in range(n):
    name, _ = input().split('\n')
    poketmon.append(name)


for i in range(m):
    if i == m - 1:
        question = input()
    else:
        question, _ = input().split('\n')

    if question.isdigit():
        # print(f'question is{question}')
        # 숫자면
        print(poketmon[int(question) - 1])
    else:
        # 이름이면 해당 숫자를 출력
        # print(f'question is no isdigit {question}')
        print(poketmon.index(question) + 1)
