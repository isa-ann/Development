'''

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.


'''


'''These variables will be placeholders for the total and new string we will be creating'''

# total = 0.0
# letter_strings = ""

# while True:
#     user_input = input("Enter a string: ")
    
#     # Check if the string is empty
#     if user_input == "":
#         break
    
#     # Check if the string is a number
#     try:
#         number = float(user_input)
#         total += number
#         continue
#     except ValueError:
#         pass
    
#     # Check if the string is a set of letters
#     if user_input.isalpha():
#         letter_strings += user_input
#         continue
    
#     # Check if the string contains symbols
#     if not user_input.isalnum():
#         continue

# # Output the results
# print("Total:", total)
# print("Concatenated letter strings:", letter_strings)

total = 0.0
letter_strings = ""

while True:
    user_input = input("Enter a string: ")
    
    # Check if the string is empty
    if user_input == "":
        break
    
    # Check if the string is a number
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):  # Handling negative numbers
        total += float(user_input)
        continue
    
    # Check if the string is a set of letters
    if user_input.isalpha():
        letter_strings += user_input
        continue
    
    # Check if the string contains symbols
    if not user_input.isalnum():
        continue

# Output the results
print("Total:", total)
print("Concatenated letter strings:", letter_strings)
