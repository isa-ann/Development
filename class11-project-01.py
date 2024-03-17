# List of taken usernames
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']

# Sign-up process
print("To sign up, enter a username and password.")
print("The password must start with a lowercase letter and only contain letters, numbers, and underscores.")
print("The password must be at least 8 characters long, contain at least one uppercase letter,")
print("contain at least one lowercase letter, contain at least one digit, contain at least one special character,")
print("and not have any spaces.")

while True:
    username = input("Please enter a username: ")
	   
    if username in taken_usernames:
        print("Username taken")
					
    elif not username.isidentifier() or not username[0].islower():
        print("Invalid username")
    else:
        break

while True:
    password = input("Please enter a password: ")
												 
	   
    if len(password) < 8:
        print("Invalid password")
					
    elif not any(p.isupper() for p in password):
        print("Invalid password")
					
    elif not any(p.islower() for p in password):
        print("Invalid password")
					
    elif not any(p.isdigit() for p in password):
        print("Invalid password")
					
    elif " " in password:
        print("Invalid password (contains spaces)")
    else:
        break

print('Sign up successful')

# Store valid username and password
valid_username = username
valid_password = password

# Login process
while True:
    login_username = input("Please enter your username to log in: ")
    login_password = input("Please enter your password to log in: ")

    if login_username == valid_username and login_password == valid_password:
        print('Login successful')
        break
    else:
        print("Invalid username or password")
