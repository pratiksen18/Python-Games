from string import ascii_lowercase, ascii_uppercase, digits, punctuation
password = input("Enter your password :: ")

def validate(values):
    for letter in password:
        if letter in values:
            return True
    return False  # optional

if len(password) >= 8:
    if validate(ascii_lowercase):
        if validate(ascii_uppercase):
            if validate(digits):
                if validate(punctuation):
                    print("Password VALID !!!! :) ")
                else:
                    print("minimim one special char required")
            else:
                print("Minimum 1 digits required !")
        else:
            print("Minimum 1 upperCase letter required")
    else:
        print("Minimum 1 lowerCase letter required !")
else:
	print("Password must contains minimim 8 char.")