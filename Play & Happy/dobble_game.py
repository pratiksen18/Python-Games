from random import choice, shuffle

words = ['goon', 'loser',  'criminal', 'carbon',  'collection',
         'helpless',  'crisis', 'adventure', 'bloodsport', 'mouse']


def get_random_word():
    # choose a random word from list of words
    rand_word = choice(words)
    # remove the word, for stop repetation
    words.remove(rand_word)
    return rand_word


def create_list_of_words():
    return [get_random_word() for _ in range(4)]


# Create two list of words (each has 4 words)
first_list = create_list_of_words()
second_list = create_list_of_words()

# Select a random word
same_word = get_random_word()
# Append the same word both in list
first_list.append(same_word)
second_list.append(same_word)

# Shuffle the list
shuffle(first_list)
shuffle(second_list)

print("\n--------------------***** FIND THE SIMILARITY *****--------------------")
print(first_list, second_list)

if input("Find the similar word:- ").lower() == same_word:
    print("CORRECT !!")
else:
    print(f"Oops! Your answer is incorrect. \nThe correct word is {same_word}")
