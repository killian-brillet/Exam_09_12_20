from colorama import init 
init() 
from colorama import Fore, Back, Style 
import random

def conditionvictoire (victoire):
    if (motjoueur = motchoisi):
        victoire = true


tableaumot = ["castor","cinema","citron","sapins","python","lettre","violet","marron","orange","avions"]
motjoueur=[" "," "," "," "," "," "]
motrandom=random.choice(tableaumot)
motchoisi=[motrandom]

victoire = false
tour = 1

print(motchoisi)
print(mot)
while (tour < 10):
    for i in range (0,6):
        if motjoueur[i] = motchoisi[i]:
            print (Back.RED + motjoueur[i], end=" ")
        if motjoueur[i] !=  motchoisi[i]:
            print (Back.BLUE + motjoueur[i], end" ")
    tour = tour + 1
    conditionvictoire (victoire)
    if (victoire = true):
        print("Bravo vous avez gagné")
        input()

if (victoire = false):
    print("Vous avez perdu, le mot etait ", motchoisi)
    

print(motchoisi)
print(mot)
input()
