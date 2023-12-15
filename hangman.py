
import random
words=["laptop", "mobilephone", "chargercable", "mouse", "pencil", "temperglass", "case", "powerbank"]
chose_the_words=random.choice(words)
print("welcome to the hangman game")
display=[]
for letter in chose_the_words:
    display += "*"
print(display)
complete_the_game=False
chances=5
while not complete_the_game:
    find_the_letter=input("Find the letter:")
    for position in range(len(chose_the_words)):
        letter=chose_the_words[position]
        if letter==find_the_letter:
            display[position]=find_the_letter
    print(display)
    if find_the_letter not in chose_the_words:
        chances-=1
        if chances==0:
            complete_the_game=True
            print(" Opps's you loose the game  Try again :) ") 
    if "*" not in display:
        print("you won the game")  

 