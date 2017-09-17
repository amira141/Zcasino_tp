#-*-coding:Latin-1 -*

import os 
from random import randrange
from math import ceil


#******Zcasino******

def QUITTER() :
    QU = input("Voulez-vous recommencer une partie ? Si oui, tapez sur entrée, si non tapez CTRL+C.")


#-Portefeuille
argent = input("Combien voulez-vous miser pour cette partie?")#l'utilisateur mise le montant qu'il souhaite pour la partie 
argent = int(argent)
continuer_partie= True

print("Vous vous installez à la table de la roulette avec",  argent, "$.")


#---Le joueur

while continuer_partie :
    numero = -1
    while numero<0 or  numero>=49 : 
        numero = input("Choisissez un numero compris entre 0 et 49 sur lequel vous souhaitez miser.") #choix du numéro sur lequel miser

        #Nombre misé uniquement compris entre 0 et 49 
        try:
            numero = int(numero)
        except ValueError:
            print("Vous n'avez pas saisi de nombres.")
            numero = -1
            continue
        if numero <0:
            print("Ce nombre est négatif")
        if numero >=49 :
            print("Ce nombre est supérieur à 49.")
     
        #mise toujours positive ou possible  
    mise = 0
    while mise <=0 or mise > argent:
        mise = input("Quelle est votre mise ?") #choix de la mise 
        

        try:
            mise = float(mise)
        except ValueError:
            print("vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0 :
            print("Cette mise n'est pas valable")
        if mise > argent:
            print("Désolé vous n'avez pas cet argent. Vous n'avez que:",argent,"$.")
            
        

#---Affichage d'un numéro entre 0 et 49 

        #numero_gagnant = randrange(50) #affichage d'un numéro au hasard entre 0 et 49 
        #print("Le numero de la case sur laquelle la bille s'est arrete est le numero:",numero_gagnant,".")


#---Gains
        
        #if numero_gagnant == numero : 
            #gains = ceil(mise + (3*M))
            #print("Bravo, vous avez gagne:",gains,"$.")
            #print(QUITTER())
            

        #elif (numero_gagnant%2 == 0 and numero%2 == 0) or (numero_gagnant%2 != 0 and numero%2 !=0): 
            #gains = ceil(mise + (1/2)*mise)
            #print("Bravo, vous avez gagne:",gains,"$.")
            #print(QUITTER())
           
            
        #else :
            #gains = ceil(mise-mise)
            #print("Malhereusement, vous avez perdu votre mise de",mise,"$.")
            #print("A present il vous reste:",gains,"$.")
            #print(QUITTER())
            
        

os.system("pause")