#Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

import sys
from time import sleep
from os import system, name
from random import randint

 

#dialog to get users choice
def textWahl():
    print("Triff deine Wahl:\n\n(1) Stein\n(2) Schere\n(3) Papier\n(0) Hilfe!! Raus hier!!\n\n")
    try:
        wahl = int(input("Nun waehle weise...\nZahl eingeben: "))
    except ValueError:
        return -1


    #statement or error message
    switch = {
        0: "\nDann lauf doch zu Mama.\n",
        1: "\nOha! Der gute alte Stein.\n",
        2: "\nUuuuuh, die Schere.\n",
        3: "\nDas Papier ist eine gute Wahl.\n"
    }
    
    if(wahl<4 and wahl >0):
        print(switch.get(wahl))
    elif wahl==0: 
        print(switch.get(wahl))
        sleep(1)
        return -2
    else:
        print("\nKannst du etwa nicht bis 3 Zaehlen???.\n")
        sleep(2)
        return -1
    return wahl;

#clear screen
def clear():
        _=system('clear')

#returns a randomized int 1 to 3
def randomChoice():
    return (randint(1,3))

#checks who is the winner
def whoWins(user, pc):
    if(user==1):
        if(pc==2):
            return 0
        if(pc==3):
            return -1
    elif(user==2):
        if(pc==1):
            return -1
        if(pc==3):
            return 0
    elif(user==3):
        if(pc==1):
            return 0
        if(pc==2):
            return -1
    else: return 1;

def goodbye():
    print("Ciao. Und danke fuer nichts.\n")
    sleep(2)

def getChoicesString(choice):
    if(choice==1):
        return "Stein"
    elif(choice==2):
        return "Schere"
    else: return "Papier"



# Main program starts here

wahl =-1

#number of wins
userCount = 0
pcCount = 0

while(wahl!=0):
    clear()
    print("\n##### Stein, Schere, Papier - V1.0 by ChrispyWugen #####\n")
    
    #shows choices and takes user choice
    wahl = textWahl()
    
    #continues for wrong inputs, exits if chosen
    if(wahl==-1):
        print("\nSoll das etwa witzig sein?\n")
        sleep(2)
        print("Versuchs noch einmal\n")
        sleep(2)
        clear()
        continue
    elif(wahl==-2):
        goodbye()
        break

    sleep(2)

    #computers turn
    print("Der Computer trifft seine Wahl. Warte kurz\n")
    pcWahl = int(randomChoice())
    result = whoWins(wahl, pcWahl)
    sleep(1)
    curString = getChoicesString(pcWahl)
    print("Er hat ",curString," gewaehlt\n")
    sleep(1)

    #prints whether win, lose or draw
    if(result==0):
        print("Du gewinnst")
        userCount += 1
    elif(result==-1):
        print("Haha. Verloren.")
        pcCount += 1
    else:print("Unentschieden.")
    sleep(2)

    #state of play
    print("\n\nAktueller Punktestand:\n")
    print("User: ",userCount,"  und  Computer: ",pcCount)
    

    #dialog for playing again or exiting
    again = input("\nNoch eine Runde?(Yes/No): ")
    if(again=="yes" or again=="y" or again == "Yes"):
        continue
    else: 
        goodbye()
        break

#quit script and return 0
sys.exit(0)
