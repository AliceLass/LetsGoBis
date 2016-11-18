# -*-coding:Utf-8 -*

"""Module envoyant la réponse finale de Comment y aller? Il est appelé par l'arbre de décision en fonction du mode de déplacement choisi"""


def reponse_walking(meta):
    '''Fonction appelée si le mode de deplacement choisi est walking'''
    origin=meta.origin
    arrival=meta.arrival
    duration_minute=meta.walking_duration//60
    duration_seconde=meta.walking_duration%60
    reponse=str("Marche depuis "+ origin.address + " jusqu'à " + arrival.address + "." + "\n" + "La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")
    return(reponse)


def reponse_velib(meta):
    '''Fonction appelée si le mode de deplacement choisi est le velib'''
    origin=meta.origin
    arrival=meta.arrival
    station_origin=meta.velibitinerary.StationOrigin
    station_arrival=meta.velibitinerary.StationArrival
    duration_minute = meta.velib_duration // 60
    duration_seconde = meta.velib_duration % 60
    reponse = str("Marche depuis " + origin.address + " jusqu'à " + station_origin.address + "." + "\n" + "Prends le vélib à la station située " + station_origin.address + " et roule jusqu'à la station située " + station_arrival.address + "\n" + "Marche depuis " + station_arrival.address + " jusqu'à " + arrival.address + "." + "\n" + "La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")
    return(reponse)


def reponse_autolib(meta):
    '''Fonction appelée si le mode de deplacement choisi est l'autolib'''
    origin=meta.origin
    arrival=meta.arrival
    station_origin=meta.autolibitinerary.StationOrigin
    station_arrival=meta.autolibitinerary.StationArrival
    duration_minute = meta.autolib_duration // 60
    duration_seconde = meta.autolib_duration % 60
    reponse = str("Marche depuis " + origin.address + " jusqu'à " + station_origin.address + "." + "\n" + "Prends l'autolib à la station située " + station_origin.address + " et roule jusqu'à la station située " + station_arrival.address + "\n" + "Marche depuis " + station_arrival.address + " jusqu'à " + arrival.address + "." + "\n" + "La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")
    return(reponse)


def reponse_transit(meta):
    '''Fonction appelée si le mode de deplacement choisi est le transit'''
    origin=meta.origin
    arrival=meta.arrival
    steps=meta.transititinerary.itinerary_steps()
    reponse = str("Marche depuis " + origin.address + " jusqu'à " + steps[0]["departure_stop"] + "." + "\n")
    for i in range(0,len(steps)):
        reponse += str("Prendre la ligne " + steps[i]["line"] + " de " + steps[i]["type"] + " en direction de " + steps[i]["direction"] + ". Descendre à " + steps[i]["arrival_stop"] + "." + "\n")
    reponse += str("Marche depuis " + steps[len(steps)-1]["arrival_stop"] + " jusqu'à " + arrival.address + "." + "\n")
    duration_minute = meta.transit_duration // 60
    duration_seconde = meta.transit_duration % 60
    reponse += str("La durée du parcours est de " + str(duration_minute) + " minutes " + str(duration_seconde) + " secondes. ")
    return(reponse)


