"""
decorator = A function that extends the behavior of another function
            w/o modifying the base function
            Pass the base function as an argument to the decorator

@add_sprinkles
get_ice_cream("vanilla") #here, get_ice_cream is the base function and add_sprinkles is the decorator
"""

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles...")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge...")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream cone! Enjoy!")

get_ice_cream("vanilla")