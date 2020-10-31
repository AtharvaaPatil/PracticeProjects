import random
name = input('Enter your name: ')
print('Good Luck ' + name)
# Opening the movie names file
file = open('Names.txt')
names = file.readlines()
name = random.choice(names)
name = name.lower()
name = str(name).strip('\n')
name = str(name).strip('\r')
print('Guess the characters: ')
guesses = str()
if ' ' in name:
    guesses += ' '
turns = 6
while turns > 0:
    failed = 0
    for char in name:
        if char in guesses:
            print(char, end=' ' )
        else:
            print('_', end=' ' )
            failed += 1
    if failed == 0:
        print('\nYou win')
        exit()
    guess = input('\n\nGuess a character: ')
    guesses += guess 
    if guess not in name:
        turns -= 1
        print('Wrong')
        print('You have' + str(turns) + 'more guesses')
    if turns == 0:
        print("You lose")
        print('The movie was: ', name)