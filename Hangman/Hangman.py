from words import words
import random as r
import string

def retry():
    ans = input("Do you wish to play/ : (y/n) : ").lower()
    if(ans == "y"):
        new_word = get_word(words)
        play_func(new_word)
    else:
        print("EXIT.")

def get_word(words):
    new_word = r.choice(words)
    while "-" in new_word or " " in new_word:
        print("This is a hyphenated word or a spaced/two word(s)")
    return new_word.upper()

def play_func(new_word):
    print("Enter 0 to exit")
    print(new_word)
    num = len(new_word)
    print(num)
    wor_let = set(new_word)
    alphab = set(string.ascii_uppercase)
    used_alphab = set()
    word_list = ["*"]
    lives = 10
    while "*" in word_list:
        guess = input("Guess a letter : ").upper()
        
        #if(len(word_list) == num): return
        if(guess == "0") : return
        if guess in alphab or (guess == "-") or guess == " ":
            if guess not in wor_let : lives -= 1
            used_alphab.add(guess)
            alphab.remove(guess)
        else :
            print("Invalid Character or Character already used. Please try again")
            lives -= 1
        print("You have used these letters : ", " ".join(used_alphab))
        word_list =  [a if a in used_alphab else "*" for a in new_word  ]
        print("The Word is : ", " ".join(word_list))
        print("Total Lives : ", lives)

        if (lives == 0) :
            print("You Lose...")
            retry()
    if lives > 0 : print("You Won!!")
    retry()


retry()




    
