 ## 2. Create a game in which the user is presented with an anagram of a word and has to guess the right word within a limited number of attempts.

anagram_word = 'ptnyho'
print("Anagram Word is  : ",anagram_word)
count = 0

while count<=5: 
    entered_word = input("Enter the correct word (in small letters).     ")

    if entered_word == 'python':
       print("Hurrah !!! you entered correct word.")
       break

    elif count == 4:
        print("You exhausted your chances  !!!")
        break
        ##raise Exception("You exhausted your chances  !!!")  

    else : 
       print("Incorrect word, Guess again")
       count = count+1
