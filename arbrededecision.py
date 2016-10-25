# -*-coding:Utf-8 -*

import arbrededecisionmoins4
import arbrededecisionplus4
import parametres


def arbre():
    ''' Fonction qui appelle l'arbre de decision adapté en fonction du nombre de passagers '''

    chargement=parametres.chargement()

    origin=parametres.addressOrigin()

    arrival=parametres.addressArrival()

    nombreDePassagers=parametres.nombreDePassagers()

    if nombreDePassagers <=4 and nombreDePassagers >0:
        arbrededecisionmoins4.arbremoins4(origin, arrival, chargement)
    elif nombreDePassagers >4:
        arbrededecisionplus4.arbreplus4(origin, arrival, chargement)


arbre()