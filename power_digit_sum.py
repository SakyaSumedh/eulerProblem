'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''
import time
from functools import reduce

start = time.time()
n = 1000

print(reduce(lambda x, y: int(x) + int(y), str(2**n)))
print(time.time() - start)