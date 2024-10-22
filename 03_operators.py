"""
Python supports several types of operators
"""

# Assignment Operators
"""
While the primary assignment operator is (arguably) '=' Python supports other types of assignment operator including:

Arithmetic assignment
'x += 3' == 'x = x + 3'
'x -= 3' == 'x = x - 3'
'x *= 3' == 'x = x * 3'
'x /= 3' == 'x = x / 3'
'x %= 3' == 'x = x % 3'
'x //= 3' == 'x = x // 3'
'x &= 3' == 'x = x & 3'
'x |= 3' == 'x = x | 3'
'x ^= 3' == 'x = x ^ 3'
'x >>= 3' == 'x = x >> 3'
'x <<= 3' == 'x = x << 3'
"""

# Arithmetic operators
"""
See '01-intro/01_arithmetic.py'
"""

# Comparison operators
"""
Comparison operators evaluate a statement and return the corresponding Boolean (i.e., either 'True' or 'False' -- case sensitive)

We'll define some variable to demo the common ones
"""
a = 7
b = 2

## Equal
print(a, "and", b, "are equal:", a == b)

## Not equal
print(a, "and", b, "are not equal:", a != b)

## Greater/less than
print(a, "is greater than", b, ":", a > b)

## Greater/less than or equal to
print(a, "is less than or equal to", b, ":", a <= b)

## is / not is
print("2 ** 2 is equal to 4:", 2 ** 2 is 4)
print("3/2 is not 7:", 3 / 2 is not 7)

# in / not in
print("'h' is in 'hello':", "h" in "hello")
print("'x' is not in 'hello':", "x" not in "hello")

# and/or
print("BOTH '2 is 2' and '5 > 7':", 2 is 2 and 5 > 7)
print("EITHER '2 is 2' or '5 > 7':", 2 is 2 or 5 > 7)

# not (reverse result)
print("2 is 2 *reversed*:", not(2 == 2))
