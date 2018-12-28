#!/usr/bin/env python3

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def add_up_to(list_in, k):
    complements = set()
    for v in list_in:
        if v in complements:
            return True
        complements.add(k-v)
    return False

assert add_up_to([10, 15, 3, 7], 17)
assert not add_up_to([10, 15, 3], 17)

