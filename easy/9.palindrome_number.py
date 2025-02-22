
#Given an integer x, return true if x is a
#palindrome, and false otherwise.

#Example:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.


def is_palindrome(x: int) -> bool:
    aux = str(x)
    return aux == aux[::-1]