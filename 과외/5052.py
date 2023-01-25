import sys


class Trie:
    def __init__(self):
        self.root = [False, [None]*10]

    def exist(self, s):
        # 접두사인지 확인하는 버전
        cur = self.root
        for c in s:
            cur = cur[1][c]
            if cur is None:
                return False
        # 접두사가 있다는거니까.
        return True

    def add(self, s):
        cur = self.root
        for c in s:
            if cur[1][c] is None:
                cur[1][c] = [False, [None] * 10]
            cur = cur[1][c]
        cur[0] = True


def input():
    return sys.stdin.readline().rstrip()


def tMain():
    N = int(input())
    # 개수

    Number = []
    # 실제 전화번호 문자열

    for i in range(N):
        Number.append(input())
    Number.sort(key=len, reverse=True)
    T = Trie()
    # 숫자도 Ascii로
    for num in Number:
        if T.exist([ord(c) - ord('0') for c in num]):
            # True면 접두사가 존재한다.
            print("NO")
            return
        T.add([ord(c) - ord('0') for c in num])

    # T = Trie()
    # # 숫자도 Ascii로
    # for num in Number[::-1]:
    #     if T.exist([ord(c) - ord('0') for c in num]):
    #         # True면 접두사가 존재한다.
    #         print("NO")
    #         return
    #     T.add([ord(c) - ord('0') for c in num])
    print("YES")


def main():
    T = int(input())
    for i in range(T):
        tMain()


if __name__ == '__main__':
    main()
