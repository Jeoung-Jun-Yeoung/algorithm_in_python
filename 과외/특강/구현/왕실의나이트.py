data = input()
row = int(data[1])
colunm = int(ord(data[0]) - int(ord('a')) + 1)

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1),
         (1, 2), (-1, 2), (1, -2), (-1, -2)]
