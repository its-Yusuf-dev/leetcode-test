# 1. how can download and watch the udemy videos
# 2. up load stuff on git hub
# The pizza prob
# print("welcome to python pizza deliveries")
# size =input("what size pizza do you want? S, M or L: ")
# peperoni = input("do you peperoni want on your pizza? Y on N: ")
# extra_cheese= input("Do you want extra cheese? Y or N:")
# if(size=='S'):
#     bill = 15
#     if(peperoni=='Y'):
#         bill+=2
# elif(size=='M'):
#     bill = 20
#     if(peperoni=='Y'):
#         bill+=3
# else:
#     bill = 25
#     if(peperoni=='Y'):
#         bill+=3
# if(extra_cheese=='Y'):
#     bill+=1
# print(f"Your total bill is {bill}")
# project "the concept of chose your own adventure book"
print("Welcome to tressureIsland\nyour mission is to find the tressure\n")
direction=input("left or right:l or r")
if direction=='l':
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