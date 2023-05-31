from typing import List, TypeVar, Tuple, TypeAlias, NamedTuple, Union
from collections.abc import Callable
from classes import typeclass
import platform, os
import collections
import datetime
import csv
import random
from art import logo


Transaction = collections.namedtuple('Transaction',['sender','amount','receiver','date'])
record = Transaction("sender", 123, "receiver", "date")
print(record)
# Transaction(sender='sender', amount=123, receiver='receiver', date='date')
print(record.amount)
print(record.date)

# convert to dictionary
print(record._asdict())
# {'sender': 'sender', 'amount': 123, 'receiver': 'receiver', 'date': 'date'}

class TransactionWithTimestamp(Transaction):
  @property
  def timestamp(self):
    return datetime.datetime.now()
  
  def __repr__(self):
    return f"TransactionWithTimestamp: {self.timestamp}, {self.date}"


twts = TransactionWithTimestamp("sender", 123, "receiver", "date")
print(twts)
# TransactionWithTimestamp: 2023-05-28 12:58:28.494041, date

# can read from a csv
# read csv
for record in map(Transaction._make, csv.reader(open("./sample.csv","rt"))):
  print(record.receiver)

# out>>>>
# Sally
# Frank
# Debby
# Charlie

# get results from database
# cursor.execute("SELECT sender,receiver,date,amount FROM transaction_table")
# for record in map(Transaction._make, cursor.fetchall()):
#   print(record.receiver)



def clear()-> None:
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")



class List(list):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        s = ", ".join(map(str, self))
        return f"List({s})"


class Tuple(tuple):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        s = ", ".join(map(str, self))
        return f"Tuple({s})"
    


list1 = List(1, 2, 3, 4, 5)



print(list1)



def cardgame():
    clear()
    print(logo)
    
    is_game_over = False

    def deal_card()-> int:
       """Return a random card from the deck"""
       cards: List[int] = List(11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
       card: int = random.choice(cards)
       return card
    
    def calculate_score(cards: List[int])-> int:
        """Return the sum of the card values in a card hand"""
        if sum(cards) == 21 and len(cards) == 2:
           return 0
       
        if 11 in cards and sum(cards) > 21:
           cards.remove(11)
           cards.append(1)

        return sum(cards)   

    user_cards: List[int] = List()
    dealer_cards: List[int] = List()

    def compare(user_score, dealer_score):
        if user_score == dealer_score:
             return "Draw 🙃"
        elif dealer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif dealer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > dealer_score:
            return "You win 😃"
        else:
            return "You lose 😤"  


    def deal_cards()-> None:
       """Deal two cards each to the User and Dealer"""
       for _ in range(2):
          user_cards.append(deal_card())
          dealer_cards.append(deal_card())

    deal_cards()

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)  
        print(
            f"""Your cards: Cards{[card for card in user_cards]} --> score: {user_score} || Dealer's first card: {dealer_cards[0]}\n"""
        )

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True
            

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(deal_cards)

    print(compare(user_score, dealer_score))
    

    # print(deal_card())

cardgame()