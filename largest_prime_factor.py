'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def largest_prime_factor(n):
	largest = -1

	while n % 2 == 0:
		largest = 2
		n /= 2

	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			largest = i
			n /= i

	if n > 2:
		largest = n
	
	return int(largest)

import time
start = time.time()
number = 600851475143
print(largest_prime_factor(number))
print(time.time() - start)
