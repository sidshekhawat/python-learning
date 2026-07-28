"""
function = a block of reusable code
           place () after the function name to invoke it

"""

def happy_birthday (name, age):
    print(f"Happy birthday to {name}")
    print(f"You're {age} years old!")
    print("Happy birthday to you ")
    print()

happy_birthday("Sid", 20)


"""
return = statement used to end a function
         and send a result back to the caller
"""

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")

print(full_name)