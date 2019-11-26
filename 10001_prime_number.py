'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from math import sqrt

number = 10001
prime_list = [2]

def check_prime(prim_list, value):
	for prime in prim_list:
		if prime > sqrt(value):
			break
		if value % prime == 0:
			return False
	return True

value = 3
while len(prime_list) < number:
	if check_prime(prime_list, value):
		prime_list.append(value)
	value += 2
prime_list.insert(0, 1)

print(prime_list[number])
