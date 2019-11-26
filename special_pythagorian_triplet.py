'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt

def pythagorean_triplet(sum):
	for a in range(1, sum // 2 - 1):
		for b in range(a, sum // 2):
			c = sqrt(a ** 2 + b ** 2)
			if c % 1 == 0 and a + b + c == sum:
				print(a, b, int(c))
				return a * b * int(c)

print(pythagorean_triplet(sum=1000))
