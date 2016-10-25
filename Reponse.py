# -*-coding:Utf-8 -*

"""Module envoyant la réponse finale de Comment y aller ?
Il est appelé par l'arbre de décision en fonction du mode de déplacement choisi"""


import MetaItinerary
import Itinerary
import ItineraryDispatch
import Point

#Réponse si le mode de déplacement choisi est walking
def reponse_walking(meta):
    origin=meta.origin
    arrival=meta.arrival
    duration_minute=meta.walking_duration//60
    duration_seconde=meta.walking_duration%60
    print("Marche depuis "+ origin.address + " jusqu'à " + arrival.adress + ".")
    print("La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")

#Réponse si le mode de déplacement choisi est le vélib
def reponse_velib(meta):
    origin=meta.origin
    arrival=meta.arrival
    station_origin=meta.velibitinerary.StationOrigin
    station_arrival=meta.velibitinerary.StationArrival
    duration_minute = meta.velib_duration // 60
    duration_seconde = meta.velib_duration % 60
    print("Marche depuis " + origin.address + " jusqu'à " + station_origin.adress + ".")
    print("Prends le vélib à la station située " + station_origin.adress + " et roule jusqu'à la station située " + station_arrival.adress )
    print("Marche depuis " + station_arrival.address + " jusqu'à " + arrival.adress + ".")
    print("La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")

#Réponse si le mode de déplacement choisi est l'autolib
def reponse_autolib(meta):
    origin=meta.origin
    arrival=meta.arrival
    station_origin=meta.autolibitinerary.StationOrigin
    station_arrival=meta.autolibitinerary.StationArrival
    duration_minute = meta.autolib_duration // 60
    duration_seconde = meta.autolib_duration % 60
    print("Marche depuis " + origin.address + " jusqu'à " + station_origin.adress + ".")
    print("Prends l'autolib à la station située " + station_origin.adress + " et roule jusqu'à la station située " + station_arrival.adress )
    print("Marche depuis " + station_arrival.address + " jusqu'à " + arrival.adress + ".")
    print("La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")

#Réponse si le mode de déplacement choisi est le transit
def reponse_transit(meta):
    origin=meta.origin
    arrival=meta.arrival
    steps=meta.transititinerary.ItinerarySteps()
    print("Marche depuis " + origin.address + " jusqu'à " + steps[0]["departure_stop"] + ".")
    for i in range(0,len(steps)):
        print("Prendre la ligne " + steps[i]["line"] + " de " + steps[i]["type"] + " en direction de " + steps[i]["direction"] + ". Descendre à " + steps[i]["arrival_stop"] + ".")
    print("Marche depuis " + steps[len(steps)-1]["arrival_stop"] + " jusqu'à " + arrival.adress + ".")
    duration_minute = meta.transit_duration // 60
    duration_seconde = meta.transit_duration % 60
    print("La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")


