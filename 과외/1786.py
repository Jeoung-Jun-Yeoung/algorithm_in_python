import sys
input = sys.stdin.readline


def findIndex(S, T):
    d, M = 257, 10**9+7

    def Hash(s):
        a = 0
        for c in s:
            a = (d * a + ord(c) % M)
        return a
    dT = 1
    for i in range(len(T)):
        dT = dT * d % M

    # dT = pow(d,T,M)

    def Roll(h, add, rm):
        return ((h * d + add) - rm * dT) % M

    ret = []
    HT, HS = Hash(T), Hash(S[:len(T)])

    if HT == HS:
        return ret.append(0)

    for i in range(1, len(S) - len(T) + 1):
        HS = Roll(HS, ord(S[i+len(T) - 1]), ord(S[i-1]))
        if HT == HS:
            ret.append(i)
    return ret


def main():

    S = input()
    T = input()

    ans = findIndex(S, T)
    print(len(ans))
    print(*[i+1 for i in ans])


if __name__ == '__main__':
    main()
