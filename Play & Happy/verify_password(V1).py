from string import ascii_lowercase, ascii_uppercase, digits, punctuation
password = input("Enter your password :: ")

if len(password) < 8:
	print("Password must contains minimim 8 char.")
else:
	lowerCase = False
	for letter in password:
		if letter in ascii_lowercase:
			lowerCase = True
			break

	if lowerCase == True:

		upperCase = False
		for letter in password:
			if letter in ascii_uppercase:
				upperCase = True
				break

		if upperCase == True:
			count = 0
			for letter in password:
				if letter in digits:
					count += 1

			if count >= 2:
				special_char = False
				for letter in password:
					if letter in punctuation:
						special_char = True
						break

				if special_char == True:
					print("Password VALID !!!! :) ")
				else:
					print("minimim one special char required")

			else:
				print("Minimum 2 digits required !")

		else:
			print("Minimum 1 upperCase letter required")

	else:
		print("Minimum 1 lowerCase letter required !")