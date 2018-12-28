#!/usr/bin/env python3

def add_up_to(list_in, k):
    complements = set()
    for v in list_in:
        if v in complements:
            return True
        complements.add(k-v)
    return False

assert add_up_to([10, 15, 3, 7], 17)
assert not add_up_to([10, 15, 3], 17)

