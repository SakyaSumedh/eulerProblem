'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largest_palindrome_product(n):
	lower_limit = '1'
	upper_limit = '9'
	
	for i in range(1, n):
		lower_limit = lower_limit + '0'
		upper_limit = upper_limit + '9'
	
	lower_limit = int(lower_limit)

	max_palindrome = 1
	for i in range(int(upper_limit), lower_limit, -1):
		for j in range(i, lower_limit, -1):
			product = i * j
			if product < max_palindrome:
				break
			if str(product) == str(product)[::-1] and product > max_palindrome:
				max_palindrome = product
	return max_palindrome

print("palindrome: ", largest_palindrome_product(3))
