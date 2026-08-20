"""
keyword arguments = an argument preceded by an identifier
                    helps with readability
                    order of arguments doesn't matter
                    1. positional, 2. default, 3. keyword, 4. arbitrary
"""

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

#hello("Yo", "Mr.", "Zelner", "Zelensky")

#hello("Yo", title = "Mr.", first = "Zelner", last = "Zelensky")  #this works
#hello("Yo", title = "Mr.", last = "Zelensky", first = "Zelner")  #this works

# hello(title = "Mr.", last = "Zelensky", first = "Zelner", "Yo")   #error: positional argument follows keyword argument