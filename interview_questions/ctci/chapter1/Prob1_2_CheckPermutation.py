import time
import unittest
from collections import defaultdict, Counter


#  Given two strings, write a method to decide if one is a permutation of the other

def check_permutation_1(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)


print(Counter("abbabbaccddbbd"))
# Counter({'b': 6, 'a': 3, 'd': 3, 'c': 2})

def check_permutation_2(a: str, b: str) -> bool: # by sort
    if len(a) != len(b):
        return False
    a, b = sorted(a), sorted(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def check_permutation_3(a: str, b: str) -> bool: # by count
    if len(a) != len(b):
        return False
    counter = [0] * 256
    for c in a:
        counter[ord(c)] += 1
    for c in b:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True

# ord() method returns the number representing the unicode code of
# a specified character
print(ord('a')) # 97




class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_1,
        check_permutation_2,
        check_permutation_3,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()

