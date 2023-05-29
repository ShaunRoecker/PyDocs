from typing import Callable, List, TypeVar, Tuple
import random
import pipe
import os, platform
from logo import logo, exiter
import time
# Global scope

enemies = 1

def increase_enemies():
    # can do this, but don't do it.
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


def increase_enemies_better():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies_better()

print(enemies)


# Global constants

PI = 3.14159
URL = "https://www.google.com"
TWITTERHANDLE = "@twitterer_person"

def clear()-> None:
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def number_guesser()-> None:
    clear()
    print(logo)
    print("Welcome to the Number Guesser Game!")
    print("I'm thinking of a number between 1 and 100\n")
    game_over = False

    EASY_LEVEL_TURNS = 10
    HARD_LEVEL_TURNS = 5

    def set_difficulty()-> int:
        game_mode = input("\nDo you want to play 'easy'(e) mode or 'hard' (h) mode: ").lower()
        if game_mode == "easy" or game_mode == "e":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    def create_number()-> int:
        number_options = [num for num in range(1, 101)]
        number = random.choice(number_options)
        return number

    def create_number_better()-> int:
        return random.randint(1, 101)
    
    number_to_guess = create_number()

    while not game_over:
        user_guess = int(input("\nMake a guess: "))
        if user_guess == number_to_guess:
            print(f"\nYou guessed correct! The number was {number_to_guess}")
            game_over = True

        elif user_guess > number_to_guess:
            print(f"{user_guess} is too high, guess again")
            num_guesses_left -= 1
            if num_guesses_left < 1:
                print("\nOut of Guesses! You Lose.")
                game_over = True

        elif user_guess < number_to_guess:
            print(f"{user_guess} is too low, guess again")
            num_guesses_left -= 1
            if num_guesses_left < 1:
                print("\nOut of Guesses! You Lose.")
                game_over = True

    def cont_play()-> bool:
        continue_play = input("\nDo you want to play again, 'Y' for yes, 'N' for no. \n").upper()
        if continue_play == 'Y':
            return True
        else:
            return False

    return cont_play()
    
 

def continue_play()-> None:
    if number_guesser():
        number_guesser()
    else:
        print(exiter)
        time.sleep(3)
        clear()





def num_guesser_2():

    EASY_LEVEL_TURNS = 10
    HARD_LEVEL_TURNS = 5

    turns = 0
    def check_answer(guess: int, answer: int, turns: int):
        if guess > answer:
            print("Too high")
            return turns - 1
        elif guess < answer:
            print("Too low")
            return turns - 1
        else:
            print(f"You got it! The answer was {answer}")

    def set_difficulty()-> int:
        level = input("\nDo you want to play 'easy' mode or 'hard' mode: ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else: 
            return HARD_LEVEL_TURNS
    
    def game():
        clear()
        print(logo)
        print("Welcome to the Number Guesser Game!")
        print("I'm thinking of a number between 1 and 100\n")
        answer = random.randint(1, 100)
        turns = set_difficulty()
        guess = 0
        while guess != answer:
            print(f"You have {turns} left!")
            guess = int(input("\nMake a guess: "))
            turns = check_answer(guess, answer, turns)
            if turns == 0:
                print("You are out of turns!")
                return
            
    game()

clear()
num_guesser_2()