# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

sum_total = 0
print("ENTER 10 NUMBERS ^-^")
for i in range(10):
    number = float(input(f"Number {i+1}: "))
    sum_total += number
print("The SUM of all numbers is equals to", sum_total)