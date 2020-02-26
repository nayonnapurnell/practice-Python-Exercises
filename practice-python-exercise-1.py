"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

#Ask the user to enter their name.
name = input("What's your name? ")

#Ask the user to enter their age.
age = input("How old are you? ")

#Determine how many years the user has until they are 100.
year = 100 - age

#subtract 100 years from the users age.

#report the 
print("Did you know that in the year " + year + "you will be 100 years old?")

