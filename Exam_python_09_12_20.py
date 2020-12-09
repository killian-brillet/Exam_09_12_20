#import colorama et random

from colorama import init 
init() 
from colorama import Fore, Back, Style 
import random

#fonctions    

def couleurmot (motjoueur, motrandom):
    for i in range (len(motjoueur)):
        if (motjoueur[i] == motrandom[i]):
            print (Back.RED + motjoueur[i], end=" ")
        #if (motjoueur[i] != motrandom[i] and motjoueur[i] == motrandom[1] or motjoueur[i] == motrandom[2] or motjoueur[i] == motrandom[3] or motjoueur[i] == motrandom[4] or motjoueur[i] == motrandom[5]):
        #    if (motjoueur[i] != motrandom[i]):
        #        print (Back.YELLOW + motjoueur[i], end=" ")
        if (motjoueur[i] != motrandom[i]):
            print (Back.BLUE + motjoueur[i], end=" ")
    return motjoueur, motrandom

#variables

tableaumot = ["castor","toucan","chaise","sapins","python","lettre","violet","marron","orange","cactus"]
motrandom=random.choice(tableaumot)
victoire = False
tour = 1

#texte intro

print (" Bienvenue à Motus! Vous devez deviner le mot en enoncant d'autres mots.")
print ("   Si la lettre s'affiche en rouge, elle est à la bonne place")
#print ("   Si elle s'affiche en jaune, elle n'est pas à la bonne place")
print ("   Si elle s'affiche en bleu, elle n'est meme pas dans le mot \n Bon jeu!")

#programme
    
while (tour <= 8 and victoire != True):
    motjoueur=str(input("Quel mot voulez vous essayer? \n"))
    if (len(motjoueur) == 6):
        couleurmot(motjoueur,motrandom)
        print (Style.RESET_ALL)
        tour = tour + 1
        if (motjoueur==motrandom):
            victoire = True
    else:
        print(" \nVeuillez rentrer un mot à 6 lettres \n")

#Fin de partie

if (victoire == True):
    print("Vous avez gagné, le mot etait bien", Back.RED + motrandom)

if (victoire == False):
    print("Vous avez perdu, le mot etait", Back.BLUE + motrandom)
    
input()