from typing import Callable
from dictionaries import programming_dictionary as pdict
from dictionaries import student_scores as scores
from dictionaries import travel_log3
import os, platform
from logo import logo




plus_two: Callable[[int], int] = lambda x: x + 2

print(plus_two(3))

res1: str = pdict["Bug"]

res2: str = pdict["bug".capitalize()]

os.system("echo 'Hello world!'")

def clear()-> None:
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")


for key in pdict:
    print(key)
    print(pdict[key])


clear()


def student_score(scores: dict[str, int])-> None:
    student_grades = {}
    for student in scores:
        score = scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds Expectations"
        elif score > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    return student_grades


print(student_score(scores))

clear()

def add_new_country(country_visited: str, times_visited: int, cities_visited: list[str])-> None:
    new_country = {
        "country": country_visited,
        "visits": times_visited,
        "cities": cities_visited,
    }
    travel_log3.append(new_country)


print(travel_log3, "\n")
add_new_country("Russia", 9, ["Moscow", "Saint Petersburg"])
print(travel_log3)


clear()

def auction_run()-> None:
    import math
    print(logo)

    def get_name()-> str:
        name = input("Enter your name: ")
        return name.capitalize()
 
    
    def get_bid_price()-> float:
        price = float(input("Enter bid price: $"))
        return round(price, 2)
    
    
    def find_highest_bidder(bidding_record):
        highest_amount = 0.0
        winner = ""
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > highest_amount:
                highest_amount = bid_amount
                winner = bidder
        formatted = "{:.2f}".format(highest_amount)
        print(f"The winner is {winner} with ${formatted}")

    
    bids = {}
    bidding_finished = False
    while not bidding_finished:
        name = get_name()
        price = get_bid_price()
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(bids)
        elif should_continue == "yes":  
            clear()


auction_run()
