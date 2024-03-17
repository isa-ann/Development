import re


''' What are some of the things we may come across while building this project'''

'''Initialization and prompt (and testing)'''



'''Handling error messages with a list (and testing)'''



'''Testing a string'''

# Example of string testing (testing for lowercase letter)


# Testing for uppercase as first letter




''' Taken usernames '''



''' Using Break and Continue to control the follow of loop'''

# If input is a number we will go through this while loop and continue through, if not, we will send the user back to the beginning

# while True:
#     user_input = input("Enter a number: ")
    
#     if not user_input.isdigit():
#         print("Please enter a valid number.")
#         continue  # Go back to the beginning of the loop
        
#     number = int(user_input)
    
#     print("Number entered:", number)
#     # Continue with other processing...


''' Password requirements '''


# At least 8 characters long

# Contains at least one uppercase letter
# def contains_uppercase(s):
#     for char in s:
#         if char.isupper():
#             return True
#     return False

# # Test the function
# string = input("Enter a string: ")
# if contains_uppercase(string):
#     print("The string contains at least one uppercase letter.")
# else:
#     print("The string does not contain any uppercase letter.")


# Even better, is the any function! Tests if any of items in iterable is true
def contains_uppercase(s):
    return any(char.isupper() for char in s)

# Test the function
string = input("Enter a string: ")
if contains_uppercase(string):
    print("The string contains at least one uppercase letter.")
else:
    print("The string does not contain any uppercase letter.")


# Or Regular Expressions match method
import re

# Function to check if a string contains at least one uppercase letter
def contains_uppercase(s):
    return bool(re.match(r'.*[A-Z].*', s))

# Test the function
string = input("Enter a string: ")
if contains_uppercase(string):
    print("The string contains at least one uppercase letter.")
else:
    print("The string does not contain any uppercase letter.")


''' Logging in and handling the loop'''

# These can represent the user id and password the user created
# sys_username = 'simonsays123'
# sys_password = 'fido1950'


# These can represent the re-authentication
# username = 'simonsays123'
# password = 'fido1950'

# Lets check for a match
