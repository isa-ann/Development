def is_valid_email(email):
    # Sanitize input
    email = email.strip()
    
    # Check if email has a dot at the third-to-last index and "@" at fifth-to-last index or earlier
    if len(email) >= 5 and email[-4] == '.' and email.find('@') <= len(email) - 5 and email.find('@') > 0 and ' ' not in email:
        return True
    return False

# Main function
def main():
    # Test with valid email address
    valid_email = "annie.djatsa@gmail.com"
    if is_valid_email(valid_email):
        print("True")
        return

    # Test with invalid email address
    invalid_email = "not a valid email"
    if is_valid_email(invalid_email):
        print("True")
        return

    print("False")

if __name__ == "__main__":
    main()
