
'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input("anastasia@gmail.com: ")


# Sanitize Data
email = email.strip()

# Test 1: It has a "." at the third-to-last index
test_1 = email[-4] == '.'

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
test_2 = (email.count('@') == 1) and (email.find('@') <= len(email) - 5)

# Test 3: There is at least one character before the "@" symbol
test_3 = email.find('@') > 0

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = ' ' not in email

# Final Test with and Keyword
is_valid_email = test_1 and test_2 and test_3 and test_4

# Print True if all conditions are met, otherwise print False
print("Is the email address valid?", is_valid_email)
