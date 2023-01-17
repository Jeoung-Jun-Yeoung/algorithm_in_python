import heapq


class RemovableHeap:
    def __init__(self):
        # A집합에서 B집합을 뺀것 S = A - B
        self.A = []  #
        self.B = []  #

    # S <- S + V
    # A - B <- A - B + V = (A + V) - B
    def push(self, v):
        heapq.heappush(self.A, v)

    # A - B <- A - B - V = A - (B+V)
    def erase(self, v):
        heapq.heappop(self.B, v)

    # A = {3,5}; B = {3}; S = {5} min S = 5가 되야하는데 3이 리턴됨

    # A = {3,5} B = {3} S = {3}

    def __len__(self):
        return len(self.A) - len(self.B)

    def min(self):
        while len(self.A) >= 1 and len(self.B) >= 1 and self.A[0] == self.B[0]:
            heapq.heappop(self.A)
            heapq.heappop(self.B)
        return self.A[0]


def solution(operations):
    minRemovableHeap = RemovableHeap()
    maxRemovableHeap = RemovableHeap()

    # minRemovableHeap과 Max의 내용은 항상 같다.
    for op in operations:
        code, no = op.split()
        no = int(no)
        if code == "I":
            minRemovableHeap.push(no)
            minRemovableHeap.push(-no)
            # insert
        elif no == 1:
            if len(minRemovableHeap) == 0:
                continue
            maxS = -maxRemovableHeap.min()
            maxRemovableHeap.erase(maxS)
            minRemovableHeap.erase(-maxS)
            # delete max
        else:
            # delete min
            if len(minRemovableHeap) == 0:
                continue
            minS = minRemovableHeap.min()
            minRemovableHeap.erase(minS)
            maxRemovableHeap.erase(-minS)
            # 일관성 유지

    if len(minRemovableHeap) == 0:
        return [0, 0]
    else:
        return [-maxRemovableHeap.min(), minRemovableHeap.min()]
