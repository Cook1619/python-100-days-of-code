# #Data types

# #String

# print("Hello"[-1])

# #Integer

# print(123 + 456)

# print(123_345_565 + 12_456)

# #Float 

# 3.14
# 56.7

# #Boolean true/false

# True
# False

# #How to check type checking
# print(type(True))

# #Type casting
# #This captures the length of your name you type in
# num_char = len(input("What is your name?\n"))
# #This changes num_char from a int to a string and saves it to a varibale
# new_num_char = str(num_char)
# #Now we can concat this in a sentence
# print("Your name has " + new_num_char + " characters")

# numbersToAdd = input("Please input a number \n")
# firstDigit = numbersToAdd[0]
# secondDigit = numbersToAdd[1]
# print(int(firstDigit) + int(secondDigit))

# print(3 * (3 + 3) / 3 - 3)

# weight = input('What is your weight?')
# height = input('What is your height?')
# result = float(weight) / (float(height) ** 2)
# resultAsInt = int(result)
# print('Your BMI is :: ' + str(resultAsInt))

# daysIn90 = 365 * 90
# weeksIn90 = 52 * 90
# monthsIn90 = 12 * 90

# yourAge = input('What is your age?\n')

# daysLeft = daysIn90 - (int(yourAge) * 365)
# weeksLeft = weeksIn90 - (int(yourAge) * 52)
# monthsLeft = monthsIn90 - (int(yourAge) * 12)

# print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")

print('Welcome to the tip calculator.')
bill = input('What was the total bill?\n')
tipAmount = input('What percentage tip would you like to give? 10, 12, or 15?\n')
numberOfPeople = input('How many people to split the bill?\n')

tipPercentage = int(tipAmount) / 100 + 1
total = (float(bill) / int(numberOfPeople)) * tipPercentage
print(round(total, 2))