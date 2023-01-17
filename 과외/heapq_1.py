class PriorityQueue:

    def __init__(self):
        self.arr = [None]

    def __len__(self):
        return len(self.arr) - 1

    def push(self, v):
        self.arr.append(v)

        idx = len(self.arr) - 1

        while idx != 1:
            if self.arr[idx//2] > self.arr[idx]:
                self.arr[idx], self.arr[idx] = \
                    self.arr[idx] = self.arr[idx//2]
                idx //= 2
            else:
                break

    def min(self):
        if len(self.arr) == 1:
            raise Exception
        return self.arr[1]

    def pop(self):
        if len(self.arr) == 1:
            raise Exception
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        self.arr.pop()

        idx = 1
        while True:
            # min_idx : idx, idx * 2, idx * 2 + 1 중 최솟값에 해당하는 번호
            min_idx = idx
            if 2*idx < len(self.arr) and self.arr[min_idx] > self.arr[2*idx]:
                min_idx = 2*idx
            if 2*idx < len(self.arr) and self.arr[min_idx] > self.arr[2*idx]:
                min_idx = 2*idx+1

            if idx == min_idx:
                return

            self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]
            idx = min_idx
