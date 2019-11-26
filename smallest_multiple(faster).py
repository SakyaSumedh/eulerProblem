def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def smallest_multiple(n):
    r = n
    for i in range(n, 2, -1):
        r = lcm(r, i - 1)
    return r

import time
start = time.time()
print(smallest_multiple(20))
print(time.time() - start)
