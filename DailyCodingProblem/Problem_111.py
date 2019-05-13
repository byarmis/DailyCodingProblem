#!/usr/bin/env python3

from collections import defaultdict

'''
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

'''

def subanagrams(word, string):
    word_letters = set(word)
    sorted_word = sorted(word)
    anagram_locs = []

    i = 0
    while i < len(string):
        letter = string[i]
        if letter not in word_letters:
            i += 1
            continue

        if sorted(string[i:i+len(word)]) == sorted_word:
            anagram_locs.append(i)

        i += 1

    return anagram_locs

assert subanagrams('ab', 'abxaba') == [0, 3, 4]
assert subanagrams('abc', 'abdcbacb') == [0, 3, 4, 5]
assert subanagrams('a', 'abdcbabc') == [0, 5]

