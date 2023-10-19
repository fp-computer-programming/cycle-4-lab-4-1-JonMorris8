"""
Create a Python file named lab_4-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Prompt the user to enter their first name and store it with an appropriate variable.
Prompt the user to enter their last name and store it with an appropriate variable.
Create a new variable for the user's full name and set it equal to the first name variable plus the last name variable. What is the result?
Is there an issue with this output? How could we fix that?

"""

#aurthor: Jon Morris
#Stores First Name
namef = input ("what is your first name?")

#stores last name
name1 = input("what is your last name?")

#Combines first and last name
name = namef + name1
print (name)

#No space between the first and last name, could be fixed by putting a space in quotes
name = namf + " " + name1
print (name)