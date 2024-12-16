import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
guessTaken = 0
guess = ''
while guess != secretNumber:
    print('Take a guess')
    guess = int(input())
    guessTaken = guessTaken + 1

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

print('Good Job ! my number is ' + str(secretNumber) + ' and you have tried ' + str(guessTaken) + ' times')
