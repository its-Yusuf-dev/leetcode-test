print("welcome to the roallercoaster!")
height=int(input("what is your height in cm?"))
if height>120:
    print("you can ride the roller soaster")
else:
    print("sorry you ahce to grow taller before you can ride.")
# comparison operators > < >= ... relation operator
# modulo give the reminder
num = int(input("Enter a number to check odd or even"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
# Nested lf/else
print("welcome tto the roller coaster!")
height = int (input("What is your height in cm?"))
age = int(input("what is your age?"))
if height >= 120:
    if age >=12:
        print("please pay $12")
    else:
        print("please pay $5")
else:
    print("sorry you have to grow taller before you can ride")
# Nested elif
print("Welcome to the roller coaster!")
height = int(input("what is your height in cm"))
if height >= 120:
    print("You can ride the roalercoster")
    age = int(input("what is your age?"))
    if age>=18:
        print("Please pay 10$")
    elif age>=12:
        print("Please pay 5$")
    else:
        print("Please pay 2$")
else:
    print("Sorry you need to grow taller before you can ride")
# Retry
print("Welcome to the roller coaster!")
height = int(input("what's your height in cm?"))
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Enter your age"))
    if age>=18:
        print("Please pay 15$")
        bill=15
    elif age >=12:
        print("Please pay 10$")
        bill=10
    else:
        print("Please pay 5$")
        bill=5
    photo = input("Do you want a photo(3$)? enter y for yes, n for no.")
    if photo == 'y':
        bill = bill + 3 # bill+=3
    print(f"Your total bill is {bill} $")
else:
    print("You need to grow taller before you can ride the roller coaster")
# The pizza prob
print("welcome to python pizza deliveries")
size =input("what size pizza do you want? S, M or L: ")
peperoni = input("do you want peperoni on your pizza? Y on N: ")
extra_cheese= input("Do you want extra cheese? Y or N: ")
if(size=='S'):
    bill = 15
    if(peperoni=='Y'):
        bill+=2
elif(size=='M'):
    bill = 20
    if(peperoni=='Y'):
        bill+=3
else:
    bill = 25
    if(peperoni=='Y'):
        bill+=3
if(extra_cheese=='Y'):
    bill+=1
print(f"Your total bill is {bill}")
# project "the concept of chose your own adventure book"
print("Welcome to tressureIsland\nyour mission is to find the tressure\n")
direction=input("left or right:l or r")
if(direction=='l'):
    print("fell in to the void\ngameover")
else:
    print("you survived.")
    direction=input("swim or wait:s or w")
    if direction=='s':
        print("got eaten by a crocodile\ngame over.")
    else:
        print("you survived.")
        direction=input("which door would you like to choose... red?, blue?, or yellow?... r or b or y: ")
        if direction== 'r':
            print("you win.")
        else:
            print("you loose. game over.")

# ASCII art is real 
# .lower() function can be applied to the input to lower case the char slash string



