""" Print a Random Number Between 1 and 6 """
# Import the random built in library in Python
import random

# Ask the user to enter the min and max value for the Die numbers, creating the Dice
# Furthermore, use a Try and Except to improve use of user input

try:
    min = int(input("Enter the minimum value of the die: "))
    max = int(input("Enter the maximum value of the die: "))
except:
    print("Invalid input, program will reset to default values.")
    min = 1
    max = 6

# Use a while loop using a variable with the value of true
again = True
while again:
# Use the randint() function to print with min & max as parameters
# Use the f-string to help return a more accurate response
    print (f"The Dice has been rolled, it landed on: {random.randint(min,max)}")
# Use the import() function to ask the user if they would like to roll again
    roll_again = input("Do you want to roll the dice again? Reply with yes / no: ")
    # Use the .lower() function to help with error handling on user input
    # Use the continue and break keywords to determine the iteration of the while loop
    if roll_again.lower() == "yes" :
        continue
    else:
        print("Thanks for playing!")
        break
