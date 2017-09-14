#-*-coding:Latin-1 -*

import os 
from random import randrange
from math import ceil


#******Zcasino******

def QUITTER() :
    QU = input("Voulez-vous recommencer une partie ? Si oui, tapez sur entree, si non tapez CTRL+C.")


#---Le joueur

i=1
while i==1:
    numero_u = input("Choisissez un numero compris entre 0 et 49 sur lequel vous souhaitez miser.") #choix du numéro sur lequel miser
    numero = int(numero_u) 

    ii = 50 #définir un nombre uniquement entre 0 et 49
    
    if 0<=numero<ii :
        
        #MISE TOUJOURS POSITIVE (to do)
        mise_u = input("Quelle est votre mise ?") #choix de la mise 
        mise = float(mise_u)
        

#---Affichage d'un numéro entre 0 et 49 

        numero_gagnant = randrange(50) #affichage d'un numéro au hasard entre 0 et 49 
        print("Le numero de la case sur laquelle la bille s'est arrete est le numero:",numero_gagnant,".")


#---Gains
        
        if numero_gagnant == numero : 
            gains = ceil(3*mise)
            print("Bravo, vous avez gagne:",gains,"$.")
            print(QUITTER())
            

        elif (numero_gagnant%2 == 0 and numero%2 == 0) or (numero_gagnant%2 != 0 and numero%2 !=0): 
            gains = ceil((1/2)*mise)
            print("Bravo, vous avez gagne:",gains,"$.")
            print(QUITTER())
           
            
        else :
            gains = ceil(0)
            print("Malhereusement, vous avez perdu votre mise de",mise,"$.")
            print("A present il vous reste:",gains,"$.")
            print(QUITTER())
            
            

    else:
        print("Le numero que vous avez saisi est incorrect.")
        

os.system("pause")
