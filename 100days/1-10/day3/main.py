
roller = False
if roller:
    print("Welcome to the roller coaster!")
    height = int(input("What is your height in cm? "))
    bill = 0
    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("How old are you? "))
        if age < 12:
            bill = 5
            print("Please pay $5.")
        elif age <= 18:
            bill = 7
            print("Please pay $7.")
        elif age >= 45 and age <= 55:
            print("Everything is going to be ok, have a free ride on us.")
        else:
            bill = 12
            print("Please pay $12.")

        wants_photo = input("Do you want a photo taken? Y or N. ")
        if wants_photo == "Y":
            bill += 3
        
        print(f"Your final bill is {bill}")

    else:
        print("Sorry, you have to grow taller before you can ride.")


modulo = False
if modulo:
    number = int(input("Which number do you want to check? "))
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")



bmi_run = False
if bmi_run:
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    bmi = round(weight / height ** 2)
    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you are of normal weight.")
    elif bmi < 30:
        print(f"Your bmi is {bmi}, you are overweight.")
    elif bmi < 35:
        print(f"Your bmi is {bmi}, you are obese.")
    else:
        print(f"Your bmi is {bmi}, you are clinically obese.")


leapyear = False
if leapyear:
    year = int(input("Which year do you want to check? "))
    def is_leap_year(year: int)-> bool:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            return True
        return False
    if is_leap_year(year):
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is not a leap year")

    
pizza_order = False
if pizza_order:
    print("Welcome to Python Pizza Deliveries")
    bill = 0
    size = input("What size pizza do you want? (S, M, or L): ")
    add_pepperoni = input("Do you  want pepperoni? (Y or N): ")
    extra_cheese = input("Do you want extra cheese? (Y or N): ")

    if size == "S":
        bill += 15
    if size == "M":
        bill += 20
    else:
        bill += 25

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
        
    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is {bill}")


love_calculator = False
if love_calculator:
    def love_match(n1: str, n2: str)-> None:
        combined = (n1 + n2).lower()
        true_sum, love_sum = 0, 0
        for char in "true":
            true_sum += combined.count(char)
        for char in "love":
            love_sum += combined.count(char)
        love_score = int(str(true_sum) + str(love_sum))
        if (love_score < 10) or (love_score > 90):
            print(f"Your love score is {love_score}, you go together like coke and mentos")
        elif (love_score >= 40) or (love_score <= 50):
            print(f"Your love score is {love_score}, you are alright together")
        else:
            print(f"Your love score is {love_score}")

    def get_name(): 
        return input("What is your name? ")
    love_match(get_name(), get_name())


treasure = True
if treasure:
    def print_treasure()-> None:
        print(
            '''
            *******************************************************************************
                    |                   |                  |                     |
            _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                    |                `"=._o`"=._      _`"=._                     |
            _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                    |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
            _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/[TomekK]
            *******************************************************************************
            '''
        )

    def run_game()-> None:
        print("Welcome to treasure Island.")
        print_treasure()
        print("Your mission is to find the treasure")
        choice1 = input('\nYou\'re at a crossroad, where do you want to go? \nType "left" or "right". ').lower()
        if choice1 == "left":
            choice2 = \
                input(
                    '''\nYou\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across. '''
                    ).lower()
            if choice2 == "wait":
                choice3 = \
                    input(
                    '''\nYou arrive at the insland unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose? '''
                    ).lower()
                if choice3 == "red":
                    print("\nThe room is full of fire. Game Over.")
                elif choice3 == "yellow":
                    print("\nYou found the treasure! You Win!")
                elif choice3 == "blue":
                    print("\nYou enter a room full of beasts. Game Over.")
                else:
                    print("\nThat door does not exist. Game Over.")
            else:
                print("\nYou got attacked by an angry trout. Game over.")
        else:
            print("\nYou fell into a hole. Game Over.")

    run_game()




        

