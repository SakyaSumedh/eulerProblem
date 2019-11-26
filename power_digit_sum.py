'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

from functools import reduce

n = 1000

print(reduce(lambda x, y: int(x) + int(y), str(2**n)))
