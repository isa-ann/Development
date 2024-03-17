


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
email = input("Hello, please enter your email address: ")
print(email)

# Sanitize Data
email = email.strip()
print(email)
# Clean input

# Test 1: It has a "." at the third-to-last index
# email = 'jrjuste@gmail.com'
# test_1 = email[-4] == '.'
# print('Test 1: Does the email have a "." at the thrird-to-last-index?, test_1)
# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email cannot be @.com
test_2 = (email[-10] == '@')
print('Test 2: Does the email have exactly one "@" symbol, at the fifth-to-last index or earlier?', test_2)
# Test 3: There is at least one character before the "@" symbol

# Test 4: It doesn’t have any spaces (doesn’t contain " ")

#Final Test with and Keyword


# End Parameter
# print('Hello', end=' ')
# print('World', end='')
# print('!', end='\n')


# Sep Parameter
# print("Today I woke up at ", 8, " am", sep='*')

'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''
# userin = input("Please enter your input: ")

# Formatted strings

long_num = 12.34567890

'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342



'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''
