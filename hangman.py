
words = []
language = input("\t\t\nChoose the language ('E' for English, 'D' for German ) : ")
# load the file coresponding to language
if language == "E" or language == "e" :
    lang="english"
    import os
    file = open("words.txt","r")
elif language=="D" or language == "d" :
    lang = "german"
    import os
    file = open("words2.txt", "r")
else:
    print("You have not typed a correct language character")

#  load all words from file in an array
for i in file:
    words.append(i)
file.close()

import  random
# shuffle the array with the save words
random.shuffle(words)
# pick the first index
rand_word2=words[0]
# strip the \n
rand_word=rand_word2.strip('\n')

print("\n\n\t\t\t\t\tHangman game with",len(words),lang,"words!!\n\n")
# print the fist and the last letter from the word and the spaces between
screen_text=rand_word[0]+(len(rand_word)-2)*" _" +" " + rand_word[len(rand_word)-1]
print(screen_text)

# if word is more than 5 letters then 7 tries else 5
tries= 7 if len(rand_word) > 5 else 5
#game statuses
game_over = False
game_win = False
# correct letters found and wrong
letters_found=[]
wrong_letters= []
# the first and the last character of the work are appended in our letters found
letters_found.append(rand_word[0])
letters_found.append(rand_word[len(rand_word)-1])

# prints the letters that are in our array and exist also at the word we need to guess
def display(found,word):
    # print first character
    print(word[0],end="")
    # the loop is basically from the 2nd letter (index 1) till the last index -1 
    for i in range(1,len(word)-1): 
        # the indexes  0 1 in our array have already the first and the last letter of random word , so below we check from the 2nd index from our array 
        if word[i] in found[2:len(word)]:
            print(" " + word[i], end='') # if the letter of the word exists in our list with found letters then print the letter
        elif word[i] not in found[2:len(word)]:
            print(" _", end='') # else print an _ for blank
    #print last character        
    print(" "+word[len(word)-1],end=" ")

# Here is the main game 
while not game_over and not game_win:
    # letters we have used
    print("\nCorrect letters found : ",letters_found[2:len(rand_word)-1])
    print("Wrong letters used : ",wrong_letters)
    guess = input("\nType a letter : ")
    # if our guess is in the word 
    if guess in rand_word[1:len(rand_word)-1]:
        # and if guess is already in our found letters
        if guess not in letters_found[2:len(rand_word)-1]: 
            # the loop is to check if there more than one instances of that letter in the word
            for i in rand_word[1:len(rand_word)-1]:
                if i is guess:
                    letters_found.append(guess)
        else:
            print("You have used that letter again")
        print("\n")
        display(letters_found,rand_word)
        if len(rand_word) == len(letters_found):
            game_win=True
    # if our guess not in word
    else:
        if guess in wrong_letters: # if have used the same wrong letter we wont lose a try
            print("You have used that letter again")
        else:
            print("Its not in the word")
            wrong_letters.append(guess)
            tries-=1
        print("Tries left :" ,tries)
        print("\n")
        display(letters_found, rand_word)
        if tries==0:
            game_over=True

if game_over:
    print("\nYou are hanged to death!")
    print("\nThe word was",rand_word)
elif game_win:
    print("\n\nYooohooo you are still alive!")

####### ======      The below code does a translation at the end using internet! its 80% accurate  ====== ######
#if lang =="german":
#   from translate import Translator
 #   translator = Translator(from_lang="de",to_lang="en")
  #  translation = translator.translate(rand_word)
   # print("The translation in english is : ",translation)
#if lang =="english":
 #   from translate import Translator
  #  translator = Translator(to_lang="de")
   # translation = translator.translate(rand_word)
   # print("The translation in german is : ",translation)
