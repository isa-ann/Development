# '''
# You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
# name, which stores the customer's name as a string
# product, which stores the product name as a string
# price, which stores the price of the product as a float
# Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
# Dear {name},
# Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
# We appreciate your business and look forward to serving you again.
# Sincerely,
# The ABC Company
# '''

name = input("Enter customer name: ")
product = input("Enter customer name: ")
price = (input(price of product))

print(f"""
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company      
""")

# name = 'Josiah Wilson'
# product = 'ABC Sneakers'
# price = 74.95343452342

# Remember to format the price