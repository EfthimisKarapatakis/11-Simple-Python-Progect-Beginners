# Write a Python program to check leap year:

myYear = int(input("Ente a year: "))

if myYear % 400 == 0 and myYear % 100 == 0:
    print(f"{myYear} is a leap year!")
elif myYear % 4 == 0 and myYear % 100 != 0:
    print(f"{myYear} is a leap year!")
else:
    print(f"{myYear} is not a leap year!")