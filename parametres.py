# -*-coding:Utf-8 -*

'''Module qui permet à l'utilisateur d'indiquer le nombre de passagers, son départ et son arrivée '''

from geopy.geocoders import Nominatim
import point
geolocator=Nominatim()

def nombre_de_passagers():
    '''Fonction qui demande a l'utilisateur le nombre de passagers en deplacement'''
    try:
        question_nombre_passagers=int(input("Combien de passagers êtes vous?"))
        if question_nombre_passagers<=0:
            raise ValueError("Le nombre de passagers indiqué est négatif")
        else:
            return question_nombre_passagers
    except ValueError:
        print("Vous n'avez pas indiqué un nombre positif")
        nombre_de_passagers()


def chargement():
    '''Fonction qui demande a l'utilisateur son chargement'''
    try:
        question_chargement=input("Êtes-vous chargé : pas du tout, un peu, beaucoup ?")
        if question_chargement != "un peu" and question_chargement != "pas du tout" and question_chargement != "beaucoup":
            raise ValueError("Le chargement ne correspond pas à une des trois propositions")
        else:
            return question_chargement
    except ValueError:
        print("Vous n'avez pas indiqué une des trois propositions")
        chargement()


 def address_origin():
     '''Fonction qui demande a l'utilisateur son point de depart'''
     try:
         question_origin_address=input("Adresse de départ?")
         question_origin_city=input("Ville de départ?")
         origin = question_origin_address + ' ' + question_origin_city
         if geolocator.geocode(origin)==None:
             raise ValueError("l'adresse de départ est non valide")
         else:
             point_origin=point.Point()
             point_origin.from_address(origin)
             return point_origin
     except ValueError:
         print("Votre adresse de départ n'est pas valide, veuillez l'indiquer de nouveau")
         address_origin()


 def address_arrival():
     try:
         question_arrival_address=input("Adresse d'arrivée?")
         question_arrival_city=input("Ville d'arrivée?")
         arrival = question_arrival_address +' '+ question_arrival_city
         if geolocator.geocode(arrival) == None:
             raise ValueError("l'adresse d'arrivée n'est pas valide")
         else:
             point_arrival = point.Point()
             point_arrival.from_address(arrival)
             return point_arrival
     except ValueError:
         print("Votre adresse d'arrivée n'est pas valide, veuillez l'indiquer de nouveau")
         address_arrival()
