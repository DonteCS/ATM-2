# programmer Donte' Rious
# Date: 10/11/2021
# Program: ATM Bank Transaction

'''
This program simulates an ATM utilizing If, Elif, & Else Statements
Nesting If statements and refresh our Comparison & Logical Operators
'''
print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users their names. Using variables
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("\nWelcome to Cash-R-Us", first_name, last_name + ", we will now set up a security pin on your account.\n")

# Set up a pin for the users to have a secure account

pin= input("please choose a 4-digit personal identification number:")

print("\nThank you",first_name + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our automated teller machine")

atm = input("Yes or no: "). lower()

print(atm)
if atm == "yes":
   print("\n************************************************************************\n")