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
def is_valid_email(email):
    # Clean data by stripping leading/trailing spaces
    email = email.strip()

    # Check if it has a "." at the third-to-last index
    dot_condition = email[-3] == "."

    # Check if it has exactly one "@" symbol, at the fifth-to-last index or earlier
    at_symbol_condition = email.count("@") == 1 and email[-5] == "@"

    # Check if there is at least one character before the "@" symbol
    char_before_at_condition = email.index("@") > 0

    # Check if it doesn't have any spaces
    no_space_condition = " " not in email

    # All conditions met, return True
    return dot_condition and at_symbol_condition and char_before_at_condition and no_space_condition

# Test with the provided email address
email = "anastasia@gmail.com"
print(is_valid_email(email))
