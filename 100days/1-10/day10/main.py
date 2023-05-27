from collections import Counter

dict1 = {"a": 1, "b": 2, "c": 3}

newDict = { k: str(v + 10) + "!" for (k, v) in zip(dict1.keys(), dict1.values()) }
print(newDict) # {'a': '11!', 'b': '12!', 'c': '13!'}

newDict2 = { k: v + "?" for (k, v) in newDict.items()}
print(newDict2) # {'a': '11!?', 'b': '12!?', 'c': '13!?'}

def transform(s: str)-> str:
    if len(s) < 10:
        return s * 2
    else:
        return s
    

newDict3 = { k: transform(v) for (k, v) in newDict2.items() }
print(newDict3) # {'a': '11!?11!?', 'b': '12!?12!?', 'c': '13!?13!?'}

def format_name(f_name: str, l_name: str)-> str:
    """Take first and last name and format it to return 
    the title case version of the name"""
    return f"{f_name.title()} {l_name.title()}"


full_name = format_name("john", "doe")
print(full_name) # John Doe

counted_str = Counter("abracadabra")
print(counted_str) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

print(list(counted_str.values())) # [5, 2, 2, 1, 1]

print(dict(counted_str)) # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

def format_name_2(f_name: str, l_name: str)-> str:
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"


full_name_2 = format_name_2("", "doe")
print(full_name_2) 

def is_leap_year(year: int)-> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def days_of_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = []
    if is_leap_year(year) and month == 2:
        return 29
    return month_days[month - 1]



# Docstrings
import os, platform
def clear()-> None:
    """Clears stdout output"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")



clear()

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

function = operations["+"]
print(function(2, 3))
clear()


def print_ops():
    for ops in operations:
        print(ops)

# def func1():
#     for k, v in operations.items():
#         print(k, v(num1, num2))

def x1():
    print_ops()
    operation_symbol = input("Pick an operation from options above: ")
    for k, v in operations.items():
        if k == operation_symbol:
            print(f"{num1} {operation_symbol} {num2} = {v(num1, num2)}")


def calculator():
    # Add
    def add(n1, n2):
        return n1 + n2

    # Subtract
    def subtract(n1, n2):
        return n1 - n2

    # Multiply
    def multiply(n1, n2):
        return n1 * n2

    # Divide
    def divide(n1, n2):
        return n1 / n2

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from options above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

        
calculator()

