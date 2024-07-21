import re

def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'    
    # Using re.match() to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
