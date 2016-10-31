# -*-coding:Utf-8 -*

''' Fichier python qui permet à l'utilisateur d'indiquer le nombre de passagers, son départ et son arrivée '''

from geopy.geocoders import Nominatim
import Point
geolocator=Nominatim()

def nombreDePassagers():
    try:
        question_nombre_passagers=int(input("Combien de passagers êtes vous?"))
        if question_nombre_passagers<=0:
            raise ValueError("Le nombre de passagers indiqué est négatif")
        else:
            return question_nombre_passagers
    except ValueError:
        print("Vous n'avez pas indiqué un nombre positif")
        nombreDePassagers()



def chargement():
   try:
       question_chargement=input("Êtes-vous chargé : pas du tout, un peu, beaucoup ?")
       if question_chargement != "un peu" and question_chargement != "pas du tout" and question_chargement != "beaucoup":
            raise ValueError("Le chargement ne correspond pas à une des trois propositions")
       else:
           return question_chargement
   except ValueError:
       print("Vous n'avez pas indiqué une des trois propositions")
       chargement()


def addressOrigin():
    try:
        question_origin_address=input("Adresse de départ?")
        question_origin_city=input("Ville de départ?")
        origin = question_origin_address + ' ' + question_origin_city
        if geolocator.geocode(origin)==None:
            raise ValueError("l'adresse de départ est non valide")
        else:
            point=Point.Point()
            point.FromAddress(origin)
            return point
    except ValueError:
        print("Votre adresse de départ n'est pas valide, veuillez l'indiquer de nouveau")
        addressOrigin()


def addressArrival():
    try:
        question_arrival_address=input("Adresse d'arrivée?")
        question_arrival_city=input("Ville d'arrivée?")
        arrival = question_arrival_address +' '+ question_arrival_city
        if geolocator.geocode(arrival) == None:
            raise ValueError("l'adresse d'arrivée n'est pas valide")
        else:
            point = Point.Point()
            point.FromAddress(arrival)
            return point
    except ValueError:
        print("Votre adresse d'arrivée n'est pas valide, veuillez l'indiquer de nouveau")
        addressArrival()
