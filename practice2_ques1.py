 ## 1. Write a program which asks the user to guess a predefined alphabet. Raise custom exceptions if the entered alphabet entered if smaller or greater than the predefined alphabet.

pre_def_letter = 'f'

user_given_letter = input("Enter a letter :  ")

if pre_def_letter > user_given_letter:
    raise Exception("Entered letter is smaller !!!  ")

elif pre_def_letter < user_given_letter:
    raise Exception("Entered letter is greated !!!  ")
else :
    raise Exception("Hurrah !!! You guessed the letter correctly !!!")
