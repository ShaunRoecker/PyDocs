from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404 | 403 | 401:
            return "Not found"
        case _:
            return "Something else"



def evaluate(point: Tuple[int, int])-> None:
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"y={y}")
        case (x, 0):
            print(f"x={x}")
        case (x, y):
            print(f"x={x}, y={y}")
        case _:
            raise ValueError("Not a point")
        

@dataclass
class Point:
    x: int
    y: int


def location(point: Point)-> None:
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere on the plane")
        case _:
            print("Not a point")


list1: List[int] = [1, 2, 3]
list2: List[int] = [1, 2, 3, 4]


def list_match(xs: List[int]):
    match xs:
        case []:
            print("empty list")
        case [1, 2]:
            print("with with 1 and 2 only")
        case [1, 2, _]:
            print("list with 1, 2, and one other number")
        case [1, 2, *rest]: # or [1, 2, *_]
            print(f"list that starts with 1, 2 and then {rest}")
        case _:
            print("Default")


list_match(list1) # list with 1, 2, and one other number
list_match(list2) # list that starts with 1, 2 and then [3, 4]


def match_point_with_guard(point: Point)-> None:
    match point:
        case Point(x, y) if x == y:
            print(f"The point {x} is equal to {y}")
        case Point(x, y):
            print("points")
        case _:
            print("Default")



# [x, y, *rest]
# (x, y, *rest)
# (x, y, *_)

# {"bandwidth": b, "latency": l}
# {"bandwidth": b, **rest}



class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


def match_color(color: Color)-> None:
    match color:
        case Color.RED:
            print("it's red")
        case Color.GREEN:
            print("it's green")
        case Color.BLUE:
            print("it's blue")



points = (Point(0, 0), Point(1, 1))

def match_on_points(points: Tuple[Point])-> None:
    match points:
        case (Point(x1, y1), Point(x2, y2) as p2):
            print(f"p2: {p2}, x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2}")
        case _:
            print("Default")


match_on_points(points) # p2: Point(x=1, y=1), x1: 0, x2: 1, y1: 0, y2: 1



