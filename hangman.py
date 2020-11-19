
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

random.shuffle(words)
rand_word2=words[0]
# strip the \n
rand_word=rand_word2.strip('\n')

print("\n\n\t\t\t\t\tHangman game with",len(words),lang,"words!!\n\n")
# print the fist and the last letter from the word and the spaces between
screen_text=rand_word[0]+(len(rand_word)-2)*" _" +" " + rand_word[len(rand_word)-1]

print(screen_text)

letters_found = [rand_word[0]]

tries= 7 if len(rand_word) > 5 else 5

game_over = False
game_win = False
letters_found=[]
wrong_letters= []
letters_found.append(rand_word[0])
letters_found.append(rand_word[len(rand_word)-1])

def display(found,word):
    print(word[0],end="")
    for i in range(1,len(word)-1):
        if word[i] in found[2:len(word)]:
            print(" " + word[i], end='')
        elif word[i] not in found[2:len(word)]:
            print(" _", end='')
    print(" "+word[len(word)-1],end=" ")


while not game_over and not game_win:
    print("\nCorrect letters found : ",letters_found[2:len(rand_word)-1])
    print("Wrong letters used : ",wrong_letters)
    guess = input("\nType a letter : ")
    if guess in rand_word[1:len(rand_word)-1]:
        if guess not in letters_found[2:len(rand_word)-1]:
            for i in rand_word[1:len(rand_word)-1]:
                if i is guess:
                    letters_found.append(guess)
        else:
            print("You have used that letter again")
        print("\n")
        display(letters_found,rand_word)
        if len(rand_word) == len(letters_found):
            game_win=True
    else:
        if guess in wrong_letters:
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
