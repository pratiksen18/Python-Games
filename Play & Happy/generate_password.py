'''WAP to check a password is secure or not.
    - 1. password must contains minimim 14 char.
    - 2. both upper and lower case, upper min 3, lower min 5.
    - 3. must contains 3 number and 3 special char.
    Bonus: Shuffle the password, for better security.'''

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

password = []

password += [random.choice(ascii_lowercase) for _ in range(5)]
password += [random.choice(ascii_uppercase) for _ in range(3)]
password += [random.choice(digits) for _ in range(3)]
password += [random.choice(punctuation) for _ in range(3)]

random.shuffle(password)
print(''.join(password))