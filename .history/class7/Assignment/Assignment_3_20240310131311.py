
# Ask user for their username
username = input("What is your username? ")

# Ask user for their password
password = input("What is your password? ")

# Create two variables called username and password and set them to any valid string values.
correct_username = "annie"
correct_password = "betty123"

# Create your conditional
if username == correct_username and password == correct_password: 
    print("Login successful.")
else:
    print("Incorrect username or password.")
