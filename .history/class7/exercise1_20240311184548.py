# '''
# Exercise

# Write some code that takes in numbers from a user one at a time. This should keep going until the user enters 0. Then print the sum of all the numbers.
# If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

# Example (no error):
# 5
# 12
# 0
# Sum: 17

# Example (error):
# 5
# 7
# c
# Error: Not a number

total = 0 # Initialize the variable total to keep track of the sum

while True:   # We start the loop
    try:
        user_input = input("Enter a number (0 to stop): ") # 
        number = float(user_input)
        if number == 0:
            break
        total += number
    except ValueError:
        print("Error: Not a number")
        break

print("Sum:", total)


