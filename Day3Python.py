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

print('Welcome to python pizza!!')
size = input("What size pizza would you like to order S, M, L?\n")
pepperoni =  input("Would you like pepperoni, Y or N?\n")
extraChesse = input("Would you like extra cheese, Y or N?\n")

bill = 0

if size == 'S':
    bill += 15
    if pepperoni == 'Y':
        bill += 2
    if extraChesse == "Y":
        bill += 1
        print(f"Your total is {bill}")
    else:
        print(f"Your total is {bill}") 
elif size == 'M':
    bill += 20
    if pepperoni == 'Y':
            bill += 3
    if extraChesse == "Y":
        bill += 1
        print(f"Your total is {bill}")
    else:
        print(f"Your total is {bill}")  
elif size == "L":
    bill += 25
    if pepperoni == 'Y':
            bill += 3
    if extraChesse == "Y":
        bill += 1
        print(f"Your total is {bill}")
    else:
        print(f"Your total is {bill}")  
