

def transform()-> None:
    fruits = ["Apple", "Peach", "Pear"]
    for fruit in fruits:
        print(fruit)

    fruitsT = list(map(lambda x: f"{x}!", fruits))
    print(fruitsT) #['Apple!', 'Peach!', 'Pear!']

    fruitsT2 = [f"{x}!" for x in fruits]
    print(fruitsT2) #['Apple!', 'Peach!', 'Pear!']

    fruitsTf = list(filter(lambda x: True if len(x) > 4 else False, fruits))
    print(fruitsTf) #['Apple', 'Peach']

    fruitsTf2 = [x for x in fruits if len(x) > 4]
    print(fruitsTf2) #['Apple', 'Peach']

    print(fruits)

transform()

def total_height()-> None:
    student_heights = [120, 149, 105, 133]
    total_height = 0
    for height in student_heights:
        total_height += height
    print(total_height) # 507
    print(sum(student_heights)) # 507

total_height() 


def num_of_students()-> None: 
    student_heights = [120, 149, 105, 133]
    num_students = 0
    for student in student_heights:
        num_students += 1
    print(num_students)  # 4
    print(len(student_heights)) # 4

num_of_students()


def max_score(scores: list[int])-> int:
    max_score = 0
    for score in scores:
        if score > max_score:
            max_score = score
    return max_score

print(max_score([77, 82, 90, 85, 88, 79, 92, 98, 85]))


students = {"John": 88, "Sarah": 85, "Sam": 82, "Daniel": 90}

def increment_scores(students: dict[str, int])-> list[int]:
    new_scores = { k: v+5 for (k, v) in zip(students.keys(), students.values()) }
    return list(new_scores.values())

print(increment_scores(students)) # [93, 90, 87, 95]


def for_loops_1()-> None:
    for num in range(1, 10):
        print(num)

for_loops_1()

list1 = [1, 2, 3, 4, 5, 6]
for i in range(len(list1)):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5

def sum100()-> int:
    return sum([x for x in range(1, 101) if x % 2 == 0])

print(sum100()) # 2550

def sum100_low()-> int:
    evens = [x for x in range(1, 101) if x % 2 == 0]
    total = 0
    for i in evens:
        total += i
    return total

print(sum100_low()) # 2550


def sum100_low2()-> int:
    total = 0
    for i in range(2, 101, 2):
        total += i
    return total

print(sum100_low2()) # 2550


def fizzbuzz(n: int, printer: bool)-> list[str]:
    def map_fizz(n: int)-> str:
        if n % 3 == 0 and n % 5 == 0:
            return "fizzbuzz"
        elif n % 3 == 0:
            return "fizz"
        elif n % 5 == 0:
            return "buzz"
        else:
            return str(n)
    list_fb = list(map(lambda x: map_fizz(x), range(1, n)))
    if printer:
        for i in list_fb:
            print(i)
        return list_fb
    else:
        return list_fb

fizzbuzz(16, True)
print(fizzbuzz(16, False))


def password_generator()-> None:
    import random
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
        'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
        'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    random.seed(random.randint(1, 1000))
    password = []
    for i in range(1, nr_letters + 1):
        password.append(random.choice(letters))

    for i in range(1, nr_symbols + 1):
        password.append(random.choice(symbols))

    for i in range(1, nr_numbers + 1):
        password.append(random.choice(numbers))

    random.shuffle(password)
    return "".join(password)
    
    

print(password_generator())








