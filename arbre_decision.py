# -*-coding:Utf-8 -*

'''Module initial recuperant les paramètres d'entree de l'utilisateur et lancant l'arbre de decision'''

import arbre_decision_moins4
import arbre_decision_plus4
import parametres


def arbre():
    ''' Fonction qui appelle l'arbre de decision adapté en fonction du nombre de passagers '''
    chargement=parametres.chargement()
    origin=parametres.address_origin()
    arrival=parametres.address_arrival()
    nombre_de_passagers=parametres.nombre_de_passagers()

    if nombre_de_passagers <=4 and nombre_de_passagers >0:
        arbre_decision_moins4.arbre_moins4(origin, arrival, chargement)
    elif nombre_de_passagers >4:
        arbre_decision_plus4.arbre_plus4(origin, arrival, chargement)