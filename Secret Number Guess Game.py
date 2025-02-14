print('>>>>>>Welcome To The Secret Number Guess Game<<<<<<')
secret_number = 3
guess_number = int(input('Guess the secret number between 1 to 9 : '))
while secret_number != guess_number:
         guess_number = int(input('Guess the secret number between 1 to 9 : '))
         
print('Congratulations!\nyou Guessed the correct secret number!')
  