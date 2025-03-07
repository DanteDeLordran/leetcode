#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
# #Every close bracket has a corresponding open bracket of the same type.

chars = {
    '(' : {
        'open' : True,
        'close' : ')'
    },
    '{' : {
        'open' : True,
        'close' : '}'
    },
    '[' : {
        'open' : True,
        'close' : ']'
    }
}

def is_valid(s: str) -> bool:
    for i in range(len(s) - 1) :
        if s[i] == '(' and s[i + 1] == ')':
            continue
        elif s[i] == '[' and s[i + 1] == ']':
            continue
        elif s[i] == '{' and s[i + 1] == '}':
            continue
        else:
            return False
    return True