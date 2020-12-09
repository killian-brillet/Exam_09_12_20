from colorama import init 
init() 
from colorama import Fore, Back, Style 
import random

def conditionvictoire (victoire):
    if (motjoueur == motrandom):
        victoire = 1

tableaumot = ["castor","cinema","citron","sapins","python","lettre","violet","marron","orange","avions"]
motrandom=random.choice(tableaumot)
victoire = 0
tour = 1

print(motrandom)
while (tour < 3):
    motjoueur=str(input("Quel mot voulez vous essayer?"))
    
    for i in range (0,6):
        if (motjoueur[i] == motrandom[i]):
            print (Back.RED + motjoueur[i], end=" ")
        if (motjoueur[i] !=  motrandom[i]):
            print (Back.BLUE + motjoueur[i], end=" ")
        print (Style.RESET_ALL)
    tour = tour + 1
    conditionvictoire (victoire)
    print ("Victoire =",victoire)


if (victoire == 0):
    print("Vous avez perdu, le mot etait", Back.BLUE + motrandom)
    
input()