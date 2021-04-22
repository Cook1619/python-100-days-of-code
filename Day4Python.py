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
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizonal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizonal -1] = 'X'





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")