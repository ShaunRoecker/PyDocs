from words import word_list
from stages import stages
import os, platform
import random


def hangman(xs: list[str])-> None:
    def clear():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    
    clear()

    from logo import logo
    print(logo)

    lives = 6
    chosen_word = random.choice(word_list)
    print(chosen_word)

    def guesser()-> str:
        guess = ""
        while len(guess) != 1:
            guess = input("Guess a letter: ").lower()
        return guess
    
    letters_chosen = []
    for i in range(len(chosen_word)):
        letters_chosen.append("_")

    end_of_game = False
    while not end_of_game:
        
        def print_lives(num_lives: int)-> None:
            if num_lives > 1:
                print(f"You have {num_lives} lives left")
            else:
                print(f"You only have {num_lives} life left!")

        print_lives(lives)
        print(xs[lives])
        print(" | ".join(letters_chosen), "\n")

        guess = guesser()

        clear()

        for index, char in enumerate(chosen_word):
            if char == guess:
                letters_chosen[index] = char

        if "_" not in letters_chosen:
            end_of_game = True
            print("You win!")

        if guess not in letters_chosen:
            print(f"You guessed {guess}, thats not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(xs[0])
                print("You lose!")


hangman(stages)


