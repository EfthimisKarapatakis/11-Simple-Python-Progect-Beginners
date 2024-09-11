# Write a python program to do arithmetical operations addition and division:

start = input("Do you wont to do addition(+) or division(/): ")
if start == '+':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the secont number: "))
    print(f"The sum is {num1 + num2}!" )
else:
    num3 = int(input("Enter the first number: "))
    num4 = int(input("Enter the secont number: "))
    if num4 == 0:
        print("Error: Division by zero is not possible!")
    else:
        print(f"The sum is {num3 / num4}!" )

a = input()