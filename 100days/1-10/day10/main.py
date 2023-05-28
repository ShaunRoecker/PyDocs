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

        
# calculator()

import functools
import operator

foldleft = lambda fn, acc, xs: functools.reduce(fn, xs, acc)

res3 = foldleft(operator.sub, 0, [1,2,3])

print(res3)

from enum import Enum



class Direction(Enum):
    North = 0
    East = 90
    South = 180
    West = 270

print(Direction.North.name) # North
print(Direction.West.value) # 270


import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
df2 = pd.DataFrame({'Data2': [101, 201, 301, 201, 151, 301, 451]})
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')

# Close the Pandas Excel writer and output the Excel file.
writer.close()



from typing import List, TypeVar, NewType, Tuple, Any


ID = NewType("ID", int)

some_id = ID(192938920)

print(some_id)


tuple: Tuple[str, int] = ("a", 2)
print(tuple)




from collections.abc import Callable

def higherOrder(fn: Callable[[int], str], num: int)-> str:
    return f"{fn(num)}!"


int_to_string: Callable[[int], str] = lambda x: str(x)

res2 = higherOrder(int_to_string, 42)

print(res2) # 42!



import time



list4 = [1, 2, 3, 4, 5, 6, 7, 8]
index = 4

left, right = list4[:index], list4[index:]
print(left, right)
# [1, 2, 3, 4] [5, 6, 7, 8]


class List(list):
    def __init__(self, *args):
        super().__init__(args)

    

    def map(self, fn):
        return [fn(i) for i in self]

    def split_at(self, index): 
        return (self[:index], self[index:])
    
    def find_all(self, item: Any)-> List[Any]:
        return List(filter(lambda x: True if item == x else False, self))

    

a = List(1, 2, 3, 4, 5, 6, 7, 8)

def double(i):
    return i * 2

print(a.map(double))


list_tuple = (l, r) = a.split_at(3)

print(list_tuple) # ([1, 2, 3], [4, 5, 6, 7, 8])
print(l) # [1, 2, 3]
print(r) # [4, 5, 6, 7, 8]


list5 = List(1, 2, 4, 3 , 42, 3, 42, 45, 42)

found = list5.find_all(42)

print(found) # [42, 42, 42]





