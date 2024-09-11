# White a Python program to check if a number is Positive, Negative or Zero:

myNum = float(input("Enter a number: "))

if myNum == 0:
    print("Your number is zero")
elif myNum > 0:
    print("Tour number is positive")
elif myNum < 0:
    print("Your number is negative")
else:
    print("Invalite input")