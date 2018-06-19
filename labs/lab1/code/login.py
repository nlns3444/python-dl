# Importing String Module to get digits (0-9) and characters (a-z, A-Z)
import string
symbols = ['$', '@', '!', '*']
# String.digits gives (0-9)
digits = list(string.digits)
# String.ascii_letters give characters (a-z,A-Z)
letters = list(string.ascii_letters)
# Asking user for password input
password = input("Enter Password,\n \t **Password must contain a digit, symbol and an upper case letter: \n")

while True:
    # Check for length of password between (6-16)
    if(len(password)>=6 and len(password)<=16):
        # Check for atleast one symbol is password, "any" returns true if atleast one condition is true
        if any(sym in password for sym in symbols):
            # Check for atleast one lower case letter
            if any(lower_letter in password for lower_letter in letters[0:26]):
                # Check for atleast one lower case letter
                if any(upper_letter in password for upper_letter in letters[26:52]):
                    # Check for atleast one number in password
                    if any(num in password for num in digits):
                        print("Password Saved")
                        # Breaking the while loop after password satisfies all conditions
                        break
                    else:
                        password = input("Password must have atleast one number: ")
                else:
                    password = input("Password must have atleast one uppercase letter: ")
            else:
                password = input("Password must have atleast one lowercase letter: ")
        else:
            password = input("Password must have atleast one Symbol: ")
    else:
        password = input("Length of password must be between (6-16): ")











