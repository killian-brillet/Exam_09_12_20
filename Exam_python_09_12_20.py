from colorama import init 
init() 
from colorama import Fore, Back, Style 
import random

def conditionvictoire (victoire):
    if (motjoueur == motchoisi):
        victoire = 1

def tableaumotrandom (motrandom):

def tableaumotjoueur ():


tableaumot = ["castor","cinema","citron","sapins","python","lettre","violet","marron","orange","avions"]
motjoueur=[" "," "," "," "," "," "]
motrandom=random.choice(tableaumot)

victoire = 0
tour = 1

print(motrandom)
print(motrandom[1])
while (tour < 10):
    motjoueur=input("Quel mot voulez vous essayer?")
    for i in range (0,6):
        if (motjoueur[i] == motchoisi[i]):
            print (Back.RED + motjoueur[i], end=" ")
        if (motjoueur[i] !=  motchoisi[i]):
            print (Back.BLUE + motjoueur[i], end=" ")
    print (motjoueur)
    tour = tour + 1
    conditionvictoire (victoire)
    if (victoire == 1):
        print("Bravo vous avez gagné")
        input()

if (victoire == 0):
    print("Vous avez perdu, le mot etait ", motchoisi)
    

print(motchoisi)
print(mot)
input()
