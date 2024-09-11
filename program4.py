# Write a python program to wap two variables:

a = input("Enter the first variable you want to change: ")
b = input("Enter the second variable you want to change: ")

print(f"Original variables: a = {a}, b = {b}")
a , b = b, a
# Or:
"""
temp = a
a = b
b = temp
"""

print(f"Swapped variables: a = {a}, b = {b}")