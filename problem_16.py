"""
https://projecteuler.net/problem=16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""

res = sum(map(int, str(2 ** 1000)))
print(res)
ANSWER = 1366
assert ANSWER == res
