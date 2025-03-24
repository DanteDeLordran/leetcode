# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# #Every close bracket has a corresponding open bracket of the same type.


def is_valid(s: str) -> bool:
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"]
    stack = []
    for char in s:
        if char in openers:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] != openers[closers.index(char)]:
                return False
            stack.pop(-1)
    return not stack


print(is_valid("()[]{}"))
