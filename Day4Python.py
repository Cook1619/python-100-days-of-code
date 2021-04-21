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

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
indexOfPerson = random.randint(0, len(names) - 1)
print(f"{names[indexOfPerson]} is going to be paying the bill tonight")