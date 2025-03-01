# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_numbers = 0
print("ENTER 10 NUMBERS ^-^")
for i in range(10):
    number = float(input(f"Number {i+1}: "))
    if number % 2 != 0:
        odd_numbers += 1
print("The total of ODD numbers is:", odd_numbers)