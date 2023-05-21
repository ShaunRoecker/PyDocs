import string
import unittest
from collections import Counter


def clean_phrase(s: str)-> bool:
    return [c for c in s.lower() if c in string.ascii_lowercase]


def is_palindrome_permutation_pythonic(s: str)-> bool:
    counter = Counter(clean_phrase(s))
    return sum(val % 2 for val in counter.values()) <= 1



def is_palindrome_permutation(phrase):
    def char_number(c):
        a = ord("a")
        z = ord("z")
        upper_a = ord("A")
        upper_z = ord("Z")
        val = ord(c)

        if a <= val <= z:
            return val - a

        if upper_a <= val <= upper_z:
            return val - upper_a
        return -1
    
    # checks if a string is a permutation of a palindrome
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1







    