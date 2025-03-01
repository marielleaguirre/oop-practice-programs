# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

print("ALL THE NUMBERS FROM 0 TO 100 EXCEPT NUMBERS ENDING IN ZERO(0)")
for x in range(101):
    if x % 10 != 0:
        print(x)