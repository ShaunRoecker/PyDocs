programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}


student_scores = {
    "John": 91,
    "Sarah": 87,
    "Sally": 79,
    "Frank": 75,
    "Charlie": 68,
}

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting list in dictionary
travel_log = {
    "France": ["Paris", "Little", "Dijon"],
    "Germany": ["Hamburg", "Berlin", "Cologne"],
}

# Nesting dictionary in dictionary
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Little", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Hamburg", "Berlin", "Cologne"],
        "total_visits": 5
    },
}

travel_log3 = [
    { "country": "France", "cities": ["Paris", "Little", "Dijon"], "visits": 12 },
    { "country": "Germany", "cities": ["Hamburg", "Berlin", "Cologne"], "visits": 5 },
]