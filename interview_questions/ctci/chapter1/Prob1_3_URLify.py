import unittest
import re


def urlify_algo(string: str, length: int) -> str:
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # replace spaces
            char_list[new_index - 3: new_index] = "%20"
            new_index -= 3
        else:
            # move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])

def urlify_pythonic(string: str, length: int) -> str:
    return string[:length].replace(" ", "%20")


def replacer(string: str, length: int)-> str:
    return re.compile("[ ]+").sub("%20", string[:length].lstrip())

print(replacer("  dsf sdf  ", 20))

class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify_algo, urlify_pythonic]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()