'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def is_multiple(x, n):
	for i in range(2, n):
		if x % i != 0:
			return False
	return True

def smallest_multiple(n):
	upper_limit = n
	while True:
		if is_multiple(n, upper_limit):
			return n
		n = n + upper_limit

print(smallest_multiple(20))
