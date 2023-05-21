import random
import my_module
from collections import Counter

def example1()-> None:
    rand_int = random.randint(1, 10)
    print(rand_int)

    print(my_module.pi)

    random_float = random.random() * 5
    print(random_float)

    love_score = random.randint(1, 100)
    print(f"Your love score is {love_score}")


def coin_flip()-> None:
    random_side = random.randint(0, 1)
    if random_side == 1:
        print("Heads")
    else:
        print("Tails")
    
coin_flip()

def states_of_america()-> None:
    states_of_america = [
        'Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 
        'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 
        'New Hampshire', 'Virginia', 'New York', 'North Carolina', 
        'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 
        'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 
        'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 
        'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 
        'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 
        'North Dakota', 'South Dakota', 'Montana', 'Washington', 
        'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 
        'Arizona', 'Alaska', 'Hawaii'
    ]
    last = states_of_america.pop(0)
    print(last)

    print(states_of_america[-1])

states_of_america()

def random_name_grab()-> None:
    names = "Bill, Sarah, John, Frank, Sally, Greg"
    names_list = names.split(", ")
    rand_index = random.randint(0, len(names_list) - 1)
    print(f"{names_list[rand_index]} was picked to foot the bill!")

random_name_grab()

def dequeue_1()-> None:
    from collections import deque
    # the dequeue, which is an implementation of a queue
    # if designed to have fast appends and pops from both ends.
    queue = deque(["Eric", "John", "Michael"])
    print(queue)
    queue.append("Terry") 
    print(queue)
    queue.append("Graham")
    print(queue)
    queue.popleft()
    print(queue)
    value = queue.popleft()
    print(value)
    value2 = queue.pop()
    print(value2)


dequeue_1()


def the_map_function()-> None:
    value = [1, 2, 3, 4, 5, 6]
    new_value = list(map(lambda x: x + 1, value))
    print(f"new value: {new_value}, and old value: {value}")
    # new value: [2, 3, 4, 5, 6, 7], and old value: [1, 2, 3, 4, 5, 6]

the_map_function()


def rock_paper_scissors()-> None:
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    
    user_choice = int(input("\n\nWhat do you want to choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)
    dictionary = {0: ["Rock", rock], 1: ["Paper", paper], 2: ["Scissors", scissors]}
    answer = f'''You chose {dictionary[user_choice][0]} -->\n{dictionary[user_choice][1]}\n
    the computer chose {dictionary[computer_choice][0]} -->\n{dictionary[computer_choice][1]}\n'''
    if user_choice == 0 and computer_choice == 2:
        print(answer, "You win!\n")
    elif computer_choice == 0 and user_choice == 2:
        print(answer, "You lose!\n")
    elif computer_choice > user_choice:
        print(answer, "You lose!\n")
    elif computer_choice == user_choice:
        print(answer, "Draw!\n")
    else:
        print("Entry error, try again!")

rock_paper_scissors()




