import random

random_no = random.randint(1,100)
print(random_no)
guessNo = 0
userGuess = None

while (random_no != userGuess):

    userGuess = int(input('Input number between 0 and 100 to take a guess.\n'))
    guessNo = guessNo  + 1

    if random_no==userGuess:
        print('Congratulations! You guessed it right.')
    else:
        if random_no > userGuess:
            print('You guessed it wrong. Please try a higher number.')
        if random_no < userGuess:
            print('You guessed it wrong. Please try a lower number.')

print (f'You took {guessNo} guesses.')


with open ('highscore.txt') as f:
    highscore = f.read()
    
if highscore == '':
    with open ('highscore.txt','w') as f:
        f.write(str(guessNo))

elif guessNo < int(highscore):
    print('Congratulations! You broke the high score.')
    with open ('highscore.txt','w') as f:
        f.write(str(guessNo))