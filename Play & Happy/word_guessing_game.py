#    word guessing GAME:
#'-------------------------'
import random
name = input("What is your name? ")
print("Welcome! ", name)
words = ['pratik', 'akash', 'raj', 'joy',
         'suraj', 'anurag', 'prasenjit', 'gopal',
         'aman', 'rohit', 'santosh', 'kiran', 'koushik',
         'hemanta', 'amit', 'himangsu', 'anupam', ]
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for name in word:
        if name in guesses:
            print(name)
        else:
            print("_")
            
            failed += 1
             
    if failed == 0:
        print("Congratulations! You Win.")
        print("The word is: ", word)
        break
    
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Oops! this letter doesn't belong to our dictionary.")
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("Sorry! You Loose")