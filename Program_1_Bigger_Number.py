# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

if number_1 > number_2:
    print("Bigger Number:", number_1)
else:
    print("Bigger Number:", number_2)