#-*-coding:Latin-1 -*

import os 
from random import randrange




#******Zcasino******


#---Le joueur

i = 1
while i==1:
    numero_u = input("Choisissez un numero compris entre 0 et 49 sur lequel vous souhaitez miser.") #choix du numéro sur lequel miser
    numero = int(numero_u) 
#définir UNIQUEMENT un nombre entre 0 et 49 

    mise_u = input("Quelle est votre mise ?") #choix de la mise 
    mise = int(mise_u)

#---Affichage d'un numéro entre 0 et 49 

    numero_gagnant = randrange(50) #affichage d'un numéro au hasard entre 0 et 49 
    print("Le numero de la case sur laquelle la bille s'est arrete est le :",numero_gagnant,".")


#---Gains

    if numero_gagnant == numero : 
        gains = mise + (3*M)
        print("Bravo, vous avez gagne:",gains,"$.")

#elif numero_gagnant/numero (comparer les parités)
	 else :
        gains = mise-mise
        print("Malhereusement, vous avez perdu votre mise de",mise,"$.")
        print("A present il vous reste:",gains,"$.")




os.system("pause")
