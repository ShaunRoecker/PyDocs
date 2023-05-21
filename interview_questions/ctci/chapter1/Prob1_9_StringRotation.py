
# 

def string_rotation(s1: str, s2: str)-> bool:
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


    
print(string_rotation("waterbottle", "ttlewaterbo")) # True

s1_times_2 = "waterbottlewaterbottle"
s2 =                "ttlewaterbo"