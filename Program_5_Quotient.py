# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

if number_2 == 0:
    print("Cannot be divided by ZERO.")
else:
    print("The QUOTIENT of the two numbers is:", number_1 / number_2)