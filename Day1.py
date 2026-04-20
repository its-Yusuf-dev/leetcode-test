print("Hello world!\nhi") #the back slash is above the enter butten.
print("Hello, "+ "Angela") #Use plus symbol to concatinate two strings.
# there are two types of errors 1. indentation errors 2. debugging errors.
name = input("What's your name?\n") # This is a input function kind of like scanf from c lang... it takes STRING input and what ever is written in it will be printed as it is.
print("Hello, World " + "\n" + "hi " + name ) # Here the variable is concatinated and printed.. also the variable must be string ig.
print("Hello "+ input("what is your name?")) # In python we can do crazy things like these... like here first the input function will be executed and then it will store the info and then the print statement will be executed/
print("Hello " + input("Enter your name..") + "!")
#Angela yu says that there is some website called Thonny.org where we can see/debug code in step by step manner... step by step evaluation
# Tip about comments: the short cut to comment out more then one line at once... first select the lines of code you want to comment out then use the short cut ctrl + /.
#variables 
name = input("what is your name?")
print(name)# Here no paranthesis is required.
#Tip : use google-> read documentation... find what you need... just fking google it... learn when needed.
# len() function
print(len(input("whats your name?(to find length)")))
username= input("enter your name (again)")
length = len(username)
print(length)
#Naming variables rules: nospace, no stating number , no keywords
# Typo means a spelling mistake / Typing mistake
# Project
print("Welcome to the band name generator")
city = input("Whats the name of the city that you grew up in")
pet_name = input("whats your pets name")
print("Your band name could be" + city + " "+ pet_name )
# This can also be done in a single statement but as we know i sure am lazy to write it again so yeah
c