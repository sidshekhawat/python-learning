"""
exception = An event that interrupts the flow of a program
            (ZeroDivisionError, TypeError, ValueError)
            1.try, 2.except, 3. finally

            try:
                # Try some code
            except Exception:
                # Handle an Exception
            finally:
                # Do some clean up
"""

try:                      #Inside the try block, we will attempt to execute code that may raise an exception.
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    print(result)

    
except ZeroDivisionError: #If a ZeroDivisionError occurs, the code inside this block will execute.
    print("You can't divide by zero!") 
except ValueError:        #If a ValueError occurs, the code inside this block will execute.
    print("You must enter a number!")
except TypeError:         #If a TypeError occurs, the code inside this block will execute.
    print("You must enter a number!")
except Exception:         #If any other exception occurs, the code inside this block will execute.
    print(f"An error occurred: {Exception}")
finally:                  #The code inside the finally block will always execute, regardless of whether an exception occurred or not.
    print("This will always run, no matter what.")

