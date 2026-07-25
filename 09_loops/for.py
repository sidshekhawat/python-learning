"""
for loops = Execute a block of code a fixed number of times.
            You can iterate over a range, string, sequence, etc.
"""

#for x in range (-5 , 6): 
#for x in reversed(range (-5 , 6)):
# for x in range (-5 , 6, 2): 
    #print(x)

for x in range (1, 21):
    if x ==13:
        continue #will skip the number, and continue the loop.
    else:
        print(x)

for x in range (1, 21):
    if x ==13:
        break #will end the loop.
    else:
        print(x)