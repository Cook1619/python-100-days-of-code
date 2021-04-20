#Conditionals
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print('You can ride the rollarcoaster!!')
# else:
#     print("Your not tall enough to ride the rollarcoaster")

#Odd or even practice
# numberToCheck = int(input("Please give me a number, and I'll tell you if its odd or even. "))

# if numberToCheck % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

#Nested Conditionals
# weight = float(input('What is your weight?'))
# height = float(input('What is your height?'))
# result = round(weight / height ** 2)

# if result < 18.5:
#     print(f"Your BMI is {result}, you are underweight.")
# elif result < 25:
#     print(f"Your BMI is {result}, you have a normal weight.")
# elif result < 30:
#     print(f"Your BMI is {result}, you are slightly overweight.")
# elif result < 35:
#     print(f"Your BMI is {result}, you are obese.")
# else:
#     print(f"Your BMI is {result}, you are clinically obese.")

# number = int(input("What year do you want to check if its a leap year? "))

# if number % 4 == 0:
#     if number % 100 == 0:
#         if number % 400 == 0:
#             print("LEAP")
#         else:
#             print("Its not a leap year")
#     else:
#         print("LEAP")
# else:
#     print("Not LEAP")

#Pizza Ordering

# print('Welcome to python pizza!!')
# size = input("What size pizza would you like to order S, M, L?\n")
# pepperoni =  input("Would you like pepperoni, Y or N?\n")
# extraChesse = input("Would you like extra cheese, Y or N?\n")

# bill = 0

# if size == 'S':
#     bill += 15
#     if pepperoni == 'Y':
#         bill += 2
#     if extraChesse == "Y":
#         bill += 1
#         print(f"Your total is {bill}")
#     else:
#         print(f"Your total is {bill}") 
# elif size == 'M':
#     bill += 20
#     if pepperoni == 'Y':
#             bill += 3
#     if extraChesse == "Y":
#         bill += 1
#         print(f"Your total is {bill}")
#     else:
#         print(f"Your total is {bill}")  
# elif size == "L":
#     bill += 25
#     if pepperoni == 'Y':
#             bill += 3
#     if extraChesse == "Y":
#         bill += 1
#         print(f"Your total is {bill}")
#     else:
#         print(f"Your total is {bill}")  

#Love Calc

# name1 = input("What is your name?\n")
# name2 = input("What is there name?\n")
# combined_string = name1 + name2

# lower_case_string = combined_string.lower()

# num1 = 0
# num2 = 0

# t = lower_case_string.count('t')
# r = lower_case_string.count('r')
# u = lower_case_string.count('u')
# e = lower_case_string.count('e')

# trueScore = t + r + u + e

# l = lower_case_string.count('l')
# o = lower_case_string.count('o')
# v = lower_case_string.count('v')
# e = lower_case_string.count('e')

# loveScore = l + o + v + e


# loveNumber = f"{trueScore}{loveScore}"

# if int(loveNumber) < 10 or int(loveNumber) > 90:
#     print(f"Your score is {loveNumber}, you go together like coke and mentos")
# elif  int(loveNumber) >= 40 and int(loveNumber) <= 50:
#     print(f"Your score is {loveNumber}, you are alright together")
# else:
#     print(f"You score is {loveNumber}")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer1 = input("Which direction would you like to go right or left?\n")
if answer1.lower() != 'left':
    print("You fell in a hole game over!!")
elif answer1.lower() == 'left':
    answer2 = input("Would you like to swim or wait?\n")
    if answer2.lower() != 'wait':
        print('Attacked by a trout you die!')
    elif answer2.lower() == 'wait':
        answer3 = input("Which door would you like to go in red, yellow, blue?\n")
        if answer3.lower() == 'red':
            print("Burned by fire GAMEOVER")
        elif answer3.lower() == 'yellow':
            print("YOU WIN!!")
        elif answer3.lower() == 'blue':
            print("Eaten by beasts!!")
        else:
            print("WRONG ANSWERS GAMEOVER")
