
#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

def add_two_numbers(l1 : list[int], l2 : list[int]):
    list1 = []
    l1.reverse()
    for num in l1:
        list1.append(f'{num}')

    l2.reverse()
    list2 = []
    for num in l2:
        list2.append(f'{num}')

    addition = int(''.join(list1)) + int(''.join(list2))
    return [f'{num}' for num in str(addition)][::-1]

print(add_two_numbers([2,4,3], [5,6,4]))
print(add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]))