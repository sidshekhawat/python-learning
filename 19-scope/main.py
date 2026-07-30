"""
variable scope = where a variable is visible and accessible
scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
"""


#Local
               
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()


#Enclosed

def func1():                   
    x = 1

    def func2():
        x = 2     #will use this as it is enclosed
        print(x)
    func2()

func1() 
# x = 2

def func1():                   
    x = 1

    def func2():
        print(x)
    func2()

func1() 
# x = 1


#Global

def func1():
    print (x)

def func2():
    print (x)

x = 3   #Global

func1()
func2()


#Built-in

from math import e   #Built-in

def func1():
    print(e)

e = 3    #Global

func1()

