# -*-coding:Latin-1 -*

import os 
from random import randrange




#******Zcasino******


#---Le joueur 

numero_u = input("Choisissez un numéro compris entre 0 et 49 sur lequel vous souhaitez miser.") #choix du numéro sur lequel miser
numero = int(numero_u) 

mise_u = input("Quelle est votre mise ?") #choix de la mise 
mise = int(mise_u)



#---Affichage d'un numéro entre 0 et 49 

numero_gagnant = randrange(50) #affichage d'un numéro au hasard entre 0 et 49 
print("Le numéro de la case sur laquelle la bille s'est arrêté est le :",numero_gagnant,".")


#---Gains




















os.system("pause")