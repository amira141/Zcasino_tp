
from encodings import utf_8
import os 
from random import randrange
from math import ceil


#******Zcasino******


#-Portefeuille
argent = input("Combien voulez-vous miser pour cette partie?")#l'utilisateur mise le montant qu'il souhaite pour la partie 
argent = int(argent)
continuer_partie= True

print("Vous vous installez à la table de la roulette avec",  argent, "$.")


#---Le joueur


while continuer_partie :

	#numéro misé uniquement compris entre 0 et 49
    numero = -1
    while numero<0 or  numero>=49 : 
        numero = input("Choisissez un numéro compris entre 0 et 49 sur lequel vous souhaitez miser.") #choix du numéro sur lequel miser
        print("Le numéro sur lequel vous misez est le numéro:",numero,".")
        
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
        mise = input("Quelle est votre mise ?")
        print("Votre mise est de:",mise,"$.")
        

        try:
            mise = float(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre.")
            mise = -1
            continue
        if mise <= 0 :
            print("Cette mise n'est pas valable.")
        if mise > argent:
            print("Désolé vous n'avez pas cet argent. Vous n'avez que:",argent,"$.")
            
        

#---Affichage d'un numéro entre 0 et 49 

    numero_gagnant = randrange(50) #affichage d'un numéro au hasard entre 0 et 49 
    print("Le numéro de la case sur laquelle la bille s'est arrêté est le numéro:",numero_gagnant,".")


#---Gains
        
    if numero_gagnant == numero : 
        gains = ceil(3*mise)
        print("Bravo, vous avez gagné:",gains,"$.")
        argent += gains    

    elif (numero_gagnant%2 == 0 and numero%2 == 0) or (numero_gagnant%2 != 0 and numero%2 !=0): 
        gains = ceil((1/2)*mise)
        print("Bravo, vous avez gagné:",gains,"$.")
        argent += gains
           
            
    else :
        print("Malhereusement, vous avez perdu votre mise de",mise,"$.")
        argent -= mise
        
    print("Votre portefeuille est de :",argent,"$.") 
        
#--Fin de partie
    if argent <=0 :
        print("Vous n'avez plus d'argent. La partie est finie. Au revoir.")
        continuer_partie = False
    else:
        QU = input("Souhaitez-vous quitter le casino? Si oui tapez Q. Sinon tapez sur une touche du clavier. "" ")
        QU = QU.upper()
        if QU == "Q":
            print("Merci. Vous quittez le casino avec",argent,"$. Au revoir.")
            continuer_partie = False
    
        
os.system("pause")