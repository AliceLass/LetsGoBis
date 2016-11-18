# -*-coding:Utf-8 -*

import arbre_decision_moins4
import arbre_decision_plus4
import parametres


def arbre():
    ''' Fonction qui appelle l'arbre de decision adapté en fonction du nombre de passagers '''

    chargement=parametres.chargement()

    origin=parametres.addressOrigin()

    arrival=parametres.addressArrival()

    nombreDePassagers=parametres.nombreDePassagers()

    if nombreDePassagers <=4 and nombreDePassagers >0:
        arbre_decision_moins4.arbremoins4(origin, arrival, chargement)
    elif nombreDePassagers >4:
        arbre_decision_plus4.arbreplus4(origin, arrival, chargement)


arbre()