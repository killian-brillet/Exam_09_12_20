from colorama import init 
init() 
from colorama import Fore, Back, Style 
import random
    
def couleurmot (motjoueur, motrandom):
    for i in range (len(motjoueur)):
        if (motjoueur[i] == motrandom[i]):
            print (Back.RED + motjoueur[i], end=" ")
        if (motjoueur[i] !=  motrandom[i]):
            print (Back.BLUE + motjoueur[i], end=" ")
        #if (motjoueur[i] != motrandom[i] and ):
        #    print (Back.YELLOW + motjoueur[i], end=" ")
        print (Style.RESET_ALL)
    return motjoueur, motrandom

tableaumot = ["castor","cinema","citron","sapins","python","lettre","violet","marron","orange","avions"]
motrandom=random.choice(tableaumot)
victoire = False
tour = 1

print (" Bienvenue à Motus! vous devez deviner le mot en enoncant d'autres mots.")
print ("   Si la lettre s'affiche en rouge, elle est à la bonne place")
print ("   Si elle s'affiche en jaune, elle n'est pas à la bonne place")
print ("   Si elle s'affiche en bleu, elle n'est meme pas dans le mot \n Bon jeu!")

while (tour <= 8 and victoire != True):
    motjoueur=str(input("Quel mot voulez vous essayer? \n"))
    if (len(motjoueur) == 6):
        couleurmot(motjoueur,motrandom)
        tour = tour + 1
        if (motjoueur==motrandom):
            victoire = True
    else:
        print(" \nVeuillez rentrer un mot à 6 lettres \n")

if (victoire == True):
    print("Vous avez gagné, le mot etait bien", Back.RED + motrandom)

if (victoire == False):
    print("Vous avez perdu, le mot etait", Back.BLUE + motrandom)
    
input()