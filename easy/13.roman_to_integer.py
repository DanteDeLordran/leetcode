

def roman_to_int(s: str) -> int:
    numbers = {
        'I': 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    value = 0
    for i in range(len(s) - 1):
        if numbers[s[i]] < numbers[s[i + 1]]:
            value -= numbers[s[i]]
        else:
            value += numbers[s[i]]
    value += numbers[s[-1]]
    return value
