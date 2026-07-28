"""
logical operators = evaluate multiple conditions (or, and, not,)
    or  = at least one condition must be True
    and = both conditions must be True
    not = inverts the condition (not False not True)
"""

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")



age = int(input("Enter your age:"))
attempt = int(input("Enter your attempt no:")) 

if 18<= age <=32 and attempt <=3:
    print("You are qualified to give the Exam")
else :
    print("Your are not qualified to give the Exam ")
