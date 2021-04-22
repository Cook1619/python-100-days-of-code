import random

# #Generating random whole numbers
# number = random.randint(0, 5)
# print(number)

# #Generating random floating point numbers
# random_float = random.random()
# print(random_float * 5)


# coinToss = random.randint(0, 1)

# if coinToss == 0:
#     print("Heads")
# else:
#     print("Tails")

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# indexOfPerson = random.randint(0, len(names) - 1)
# print(f"{names[indexOfPerson]} is going to be paying the bill tonight")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# print(fruits)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# horizonal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizonal -1] = 'X'





# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if player_choice >= 3 or player_choice < 0:
    print("INVALID NUMBERS YOU LOSE")
else:
    print(choices[player_choice])
    print("Computer chose:")
    print(choices[computer_choice])



    if player_choice == 0 and computer_choice == 1:
        print("You lose")
    elif player_choice == 1 and computer_choice == 0:
        print("You win")
    elif player_choice == 1 and computer_choice == 2:
        print("You lose")
    elif player_choice == 2 and computer_choice == 1:
        print("You win")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose")
    elif player_choice == 0 and computer_choice == 2:
        print("You lose")
    elif player_choice ==  computer_choice:
        print("DRAW!!")





