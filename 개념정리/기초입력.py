# 입력이 다음과 같이 주어짐
# 1 2
# a, b = map(int, input.split())


# 입력 출력 가속
# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write

# 배열입력
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# pythonic code
# map = [list(map(int, input().split())) for _ in range(int(input()))]
# 설명 []로 일단 리스트 하나를 감쌈. 2차원 배열이기에 배열안에 배열이 있어야함. 그래서 배열의 요소가 List임
# 이때 그 해당 리스트의 요소는 입력을 스플릿 해서 int형으로 map한다. 이걸 그리고 반복한다.

# 정수와 배열이 같은줄에 오는 경우
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25
# N, *arr = map(int,input().split())

# 문자열을 한글자씩 배열에 저장
# 3
# AAAA
# ABCA
# AAAA
# arr = [['A', 'A', 'A', 'A']
#        ['A', 'B', 'C', 'A']
#        ['A', 'A', 'A', 'A']] <= 요렇게

# arr = [list(input()) for _ in range(N)]

# 참고 글자 단위로 안자르려면 arr = [input() for _ in range(N)] <= 요렇게 하면 됨

# 배열 출력
# arr = [1,2,3,4]
# 1234 로 출력하려면
# print("".join(map(str,arr)))
# 그냥 1 2 3 4 로 출력은
# print(*arr)

# 문자열 거꾸로
# alph = "ABCD"
# alph[::-1]

# "DCBA" -> -1은 거꾸로라는 의미다.

# 아스키
# ord() -> 문자를 아스키, chr() -> 아스키를 문자로

# 배열 초기화 ***
# 3 5 3 행 5열

# N, M = map(int, input().split())
# arr = [[0] * N for _ in range(M)]

# 배열 원소 개수

# list.count()

# 원소 중복 제거
# alpha = list(set(alpha))

# 2차원 리스트인 경우 list(set(map(tuple,lst)))

# 배열 정렬

# arr.sort()
# arr.sort(reverse=True)
# arr.sort(key=lambda x:(x[0], x[1]))

# 조합
# from itertools import combinations
# print(list(combinations([1,2,3,4],3)))

# 순열
# from itertools import permutations
# print(list(permutations(arr, M)))

# counter
# from itertools import Counter
# val = Counter(arr).most_common()
