#!/usr/bin/python
number = 20
guess = int(input('Enter an integer: '))

if guess == number:
     print ('you guessed it.')
elif guess < number:
    print('No, it is higher than that')
else:
    print('No, it is lower than that')
