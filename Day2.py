# Subscripting 
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print("123" + "456")
# Integer = wholenumber
print(123+456)# this will give the sum
print(123_456_789)# here the under scores are fore the  commas
#float floating point like 9.5 
#boolean 
print(True)
print(False)
#len(123)
#type error the len function only accepts the string args ig
# the type function is used to find the type of the string or the args
print(type("Hello"))
print(type(123))
print(type(True))
print(type(123.45))
print(type("123"))
print(int("123")+int("456"))
#if abc is tried to be converted to int  we get a value error
print("Number of letters in your name, " + str(len(input("Enter your name "))))
print("Number of letters in your name, " + str(len(input("what is your name? "))))
#The type castinginnginginginginginginginginginginginnginginginginginginginginginginginginginginginginginginginginnginginginging
#str(len("..."))......str() int() float() bool()
#str + str is concatination 
# operators
# 6+6=12
# 6-6=0
# 6*6=36
# 5/3=1.6666
# 2**3=8
# PEMDas or the left to right 
# Tip: lets say that we need 12% of x we can do X * 0.12 ... or if we need to add more 12% we can do X *1.12
# the precidence is that  brackets(), expontents** then multiply*, devide/ then add+, subtract-
#find Bmi ( body mass index)
# BMI =weight/(height(cm)**2) ... weight in kg by square of the height in cm
# the round function
round(123.456,2) # here 2 represents the no of decimal digts to round... this will return 123.45 if used
#round(BMI,2)
#the incrementing or the short cut ways to write stuff
score = 0
score = score + 1
score += 1
score -= 1
print("Score = "+ str(score))# research
#fstring... its the better way of writing the stuff
height =1
print(f"Your score is ={score},\nyour height is{height}.\nyou are wine is {bool}")
#Project : Tip calculator 
print("Welcome to the Tip Calculator!\n")
bill = int(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, of 15% "))
total_people = int(input("How many people to split the bill?\n"))
split = (bill + bill * (tip/100))/ total_people
print(f"Each person should pay {split}")



