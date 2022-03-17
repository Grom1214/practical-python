
input("hello, what is your name?\n") 

import random
num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')