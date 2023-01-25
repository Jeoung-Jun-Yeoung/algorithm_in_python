class Trie:

    def __init__(self):
        self.root = [False, [None]*26]
        # 실제로 들어 있는지 아닌지, 두번째것은 노드에서 나가는 화살표를 담는다.

    def exit(self, s):
        cur = self.root
        for c in s:
            cur = cur[1][c]
            if cur is None:
                return False
        return True
        # 한줄로 접두사 인지 아닌지 유무를 판단할 수 있다.

    def add(self, s):
        cur = self.root
        for c in s:
            if cur[1][c] is None:
                cur[1][c] = [False, [None] * 26]
            cur = cur[1][c]
        cur[0] = True


def main():
    N, M = map(int, input().split())

    T = Trie()
    for i in range(N):
        s = input()
        T.add([ord(c) - ord('a') for c in s])

    ans = 0
    for i in range(M):
        s = input()
        if T.exit([ord(c) - ord('a') for c in s]):
            # 문자열 대신에 0부터 25까지의 수를 넘겨준다.
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
