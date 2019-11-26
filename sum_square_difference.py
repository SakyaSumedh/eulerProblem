'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_difference(n):
	# 1**2 + 2**2 + 3**2 + ... + n**2 = n(n+1)(2n+1)/6
	sum_of_square_of_n = n * (n + 1) * (2 * n + 1) / 6
	# (1 + 2 + 3 + ... + n) ** 2 = (n(n+1)/2)**2
	square_of_sum_of_n = (n * (n + 1) / 2) ** 2
	return int(square_of_sum_of_n - sum_of_square_of_n)

print(sum_square_difference(100))
