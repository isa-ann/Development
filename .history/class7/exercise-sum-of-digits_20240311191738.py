# Exercise:
# Sum of Even Digits

# Take a string as user input, and verify that it's a number.
# Loop through each digit of the number, and only add it to the sum if it's even.
# Print the sum of all the even digits at the end. 
# Make sure to use the continue keyword.
# '''




# ''' Break, Continue, and Pass '''

# User Input
while True:
    number_str = input("Enter a number: ")
    if number_str.isdigit():
        break
    else:
        print("Invalid input. Please enter a valid number.")

# Sum Calculation
even_sum = 0

# Loop through each digit
for digit in number_str:
    # Convert digit to integer
    digit_int = int(digit)
    
    # Check if the digit is even
    if digit_int % 2 == 0:
        even_sum += digit_int

# Print the sum of even digits
print("Sum of even digits:", even_sum)




# User Input with Validation: 

