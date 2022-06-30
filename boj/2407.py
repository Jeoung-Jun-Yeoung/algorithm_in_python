import math
import sys

n, m = map(int, sys.stdin.readline().split())

numerator = int(math.factorial(n))
denominator = int(math.factorial(m)) * int(math.factorial(n - m))
rst = int(numerator // denominator)
print(rst)

# / 와 // 차이가 있다. 정수를 나누고 결과를 보고 싶을때는 int를 씌우는것 말고도 //를 사용해주어야 한다.
