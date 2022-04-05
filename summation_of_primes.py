"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time

start = time.time()


def is_number_prime(primes_list, number):
    for prime in primes_list:
        if number % prime == 0:
            return False
        if number < prime * prime:
            break
    return True


def summation_of_primes(upper_limit):
    least_prime_number = 2
    primes_list = [least_prime_number] if upper_limit > least_prime_number else []
    next_prime_number = 3
    if len(primes_list):
        while next_prime_number < upper_limit:
            if is_number_prime(primes_list, next_prime_number):
                primes_list.append(next_prime_number)
            next_prime_number += 2
    return sum(primes_list)


print(summation_of_primes(upper_limit=2000000))
print(time.time() - start)
