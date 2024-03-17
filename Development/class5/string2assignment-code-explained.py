def is_valid_email(email): # This line defines a function named is_valid_email that takes an email as its argument.
    # Sanitize input
    email = email.strip() # This line removes any leading or trailing whitespace from the email address using the .strip()
    
    # Check if email has a dot at the third-to-last index and "@" at fifth-to-last index or earlier
    if len(email) >= 5 and email[-4] == '.' and email.find('@') <= len(email) - 5 and email.find('@') > 0 and ' ' not in email: # This line is a condition checking if the email address satisfies all the specified conditions:
        return True
    return False

# Main function
def main(): # This line defines a function named main() which serves as the entry point of the program.
    # Test with valid email address
    valid_email = "annie.djatsa@gmail.com" # This line defines a variable valid_email containing a valid email address to be tested.
    if is_valid_email(valid_email): # This line calls the is_valid_email function with valid_email as its argument and checks if it returns True.
        print("True") # If the email address is valid, this line prints "True".
        return # This line exits the function, ensuring that "True" is printed only once.

    # Test with invalid email address
    invalid_email = "not a valid email" # This line defines a variable invalid_email containing an invalid email address to be tested.
    if is_valid_email(invalid_email): # This line calls the is_valid_email function with invalid_email as its argument and checks if it returns True.
        print("True")
        return

    print("False")

if __name__ == "__main__": # This line checks if the script is being run directly 
    main() # This line calls the main() function, initiating the execution of the program.
