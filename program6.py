# Write a python program to convert kilometers to miles

kilometers = float(input("Enter distance in kilometers: "))

convertion_factor = 0.621371

miles = kilometers * convertion_factor

print(f"{kilometers} kilometers is {"%.3f" % miles} miles")