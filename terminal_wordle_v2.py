import random
from dictionary import word_list,dictionary

class colors:
    GREENBOX='\033[42m'
    YELLOWBOX='\033[43m'
    GREYBOX='\033[100m'
    YELLOWWARNING = '\033[93m'
    REDFAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def get_input():
    guess=input("Type in your guess: ").lower()
    while (guess not in word_list) and (guess not in dictionary):
        guess=input("Not in word list! Please try again: ").lower()
    return guess

def word_score(guess):
    letter=""
    for i in range(5):
        if guess[i] in word:
            if guess[i]==word[i]:
                letter+=f"{colors.GREENBOX}{guess[i].upper()}{colors.ENDC}"
                keyboard_update(guess[i],colors.GREENBOX)
            else:
                letter+=f"{colors.YELLOWBOX}{guess[i].upper()}{colors.ENDC}"
                keyboard_update(guess[i],colors.YELLOWBOX)
        else:
            letter+=f"{colors.GREYBOX}{guess[i].upper()}{colors.ENDC}"
            keyboard_update(guess[i],colors.GREYBOX)
    print(letter)

def keyboard_update(letter,color):
    letter=letter.upper()
    if keyboard[letter]==colors.GREENBOX:
        pass
    else:
        keyboard[letter]=color

def keyboard_printer():
    print(f"  {keyboard['Q']} Q {keyboard['W']} W {keyboard['E']} E {keyboard['R']} R {keyboard['T']} T {keyboard['Y']} Y {keyboard['U']} U {keyboard['I']} I {keyboard['O']} O {keyboard['P']} P {colors.ENDC}")
    print(f"   {keyboard['A']} A {keyboard['S']} S {keyboard['D']} D {keyboard['F']} F {keyboard['G']} G {keyboard['H']} H {keyboard['J']} J {keyboard['K']} K {keyboard['L']} L {colors.ENDC}")
    print(f"    {keyboard['Z']} Z {keyboard['X']} X {keyboard['C']} C {keyboard['V']} V {keyboard['B']} B {keyboard['N']} N {keyboard['M']} M {colors.ENDC}")

while True:
    word=word_list[random.randint(0,len(word_list)-1)]
    print(f"{colors.GREYBOX}A new word{colors.ENDC} {colors.YELLOWBOX}has been selected...{colors.ENDC} {colors.GREENBOX}Good luck!{colors.ENDC}")
    win=False
    lives=6
    keyboard={"A":f"{colors.ENDC}","B":f"{colors.ENDC}","C":f"{colors.ENDC}","D":f"{colors.ENDC}","E":f"{colors.ENDC}",
              "F":f"{colors.ENDC}","G":f"{colors.ENDC}","H":f"{colors.ENDC}","I":f"{colors.ENDC}","J":f"{colors.ENDC}",
              "K":f"{colors.ENDC}","L":f"{colors.ENDC}","M":f"{colors.ENDC}","N":f"{colors.ENDC}","O":f"{colors.ENDC}",
              "P":f"{colors.ENDC}","Q":f"{colors.ENDC}","R":f"{colors.ENDC}","S":f"{colors.ENDC}","T":f"{colors.ENDC}",
              "U":f"{colors.ENDC}","V":f"{colors.ENDC}","W":f"{colors.ENDC}","X":f"{colors.ENDC}","Y":f"{colors.ENDC}",
              "Z":f"{colors.ENDC}"}
    while lives>0:
        lives-=1
        keyboard_printer()
        guess=get_input()
        if guess==word:
            win=True
            print(f"{colors.GREENBOX}{guess.upper()}{colors.ENDC}")
            break
        else:
            word_score(guess)
            if lives>1:
                print(f"You have {colors.BOLD}{lives}{colors.ENDC} attempts left.")
            elif lives==1:
                print(f"{colors.YELLOWWARNING}You only have {colors.BOLD}1{colors.ENDC}{colors.YELLOWWARNING} attempt left!{colors.ENDC}")
    if win:
        print(f"Well done! You have won using {6-lives} attempts!")
    else:
        print(f"Oh, no... Better luck next time! The mistery word was: {colors.BOLD}{colors.REDFAIL}{word.upper()}{colors.ENDC}")
    replay=int(input("Enter 1 to play again or 0 to end the game: "))
    if not replay:
        break

print(f"{colors.GREENBOX}Bye bye!{colors.ENDC} {colors.YELLOWBOX}See you{colors.ENDC} {colors.GREYBOX}next time!{colors.ENDC}")