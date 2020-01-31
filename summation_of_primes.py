'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time
from math import sqrt

start = time.time()

def check_prime(primes_list, number):
	for prime in primes_list:
		if number % prime == 0:
			return False
		if number < prime * prime:
			break
	return True

def summation_of_primes(upper_limit):
	# primes_list = [2, 3] if upper_limit > 3 else []
	# n = 1
	# while True:
	# 	lower = 6 * n - 1
	# 	upper = 6 * n + 1

	# 	if lower > upper_limit:
	# 		break

	# 	if check_prime(primes_list, lower):
	# 		primes_list.append(lower)

	# 	if upper > upper_limit:
	# 		break

	# 	if check_prime(primes_list, upper):
	# 		primes_list.append(upper)

	# 	n += 1
	primes_list = [2] if upper_limit > 2 else []
	value = 3
	while primes_list[-1] < upper_limit:
		if check_prime(primes_list, value):
			primes_list.append(value)
		value += 2
	return sum(primes_list)

print(summation_of_primes(upper_limit=2000000))
print(time.time() - start)
