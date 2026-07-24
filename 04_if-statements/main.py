"""
if = Do some code only IF condition is true
     Else do something else
"""

#age = int(input("Enter your age:"))

#if age >= 18:
    #print("You are now signed up")
#else:
    #print("You must be 18+ to sign up")


age = int(input("Enter your age:"))
attempt = int(input("Enter your attempt no:"))

if age >= 18:
    print("You are qualified to give the Exam")
else:
    print("Your are not in the qualifying age to attempt the exam")

if attempt <= 3:
    print("You can give the exam")
else:
    print("You are out of attempts")

 