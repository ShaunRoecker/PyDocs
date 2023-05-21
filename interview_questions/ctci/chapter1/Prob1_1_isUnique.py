import time
import unittest
from collections import defaultdict


# Implement an algorithm to determine if a String has all unique characters or not.
##########################################
def is_unique_1(string: str) -> bool: 
    return len(set(string)) == len(string)


def is_unique_2(string: str) -> bool:
    characters_seen = set()
    for char in string:
        if char in characters_seen:
            return False
        characters_seen.add(char)
    return True


#  O(NlogN)
def is_unique_3(string: str) -> bool:
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True

##########################################
class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_1,
        is_unique_2,
        is_unique_3,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars_funcs in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars_funcs(text) == expected
                    ), f"{is_unique_chars_funcs.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars_funcs.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
















print(isUnique1("nodups")) #true
print(isUnique1("hasdups")) #false

print(isUnique2("nodups")) #true
print(isUnique2("hasdups")) #false
