"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import operator
import functools

lim = 100
factorial = functools.reduce(operator.mul, range(1, lim+1))
stringify = str(factorial)
res = sum(map(int, stringify))
print(res)
ANSWER = 648
assert ANSWER == res