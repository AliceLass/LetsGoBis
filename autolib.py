# -*-coding:Utf-8 -*

"""Module permettant de trouver la station autolib la plus proche en prenant en entrée un point de la classe Point"""

import requests


def _url(point):
    '''Fonction qui crée l'URL avec les coordonnées GPS long, lat et une distance D'''
    D=500
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations_et_espaces_autolib_de_la_metropole_parisienne&facet=ville&facet=type&facet=cp&refine.ville=Paris&geofilter.distance='+str(point.latitude)+'%2C+'+str(point.longitude)+'%2C'+str(D)
    return chaine

def get_autolib(point):
    '''Fonction qui retourne le JSON avec les stations autolib correspondant à URL'''
    return requests.get(_url(point))

def autolib(point):
    '''Fonction qui retourne la station autolib la plus proche et son adresse'''
    autolib_json=get_autolib(point).json()
    DMIN = 500
    station_min = []
    adresse_station_min=""

    for i in autolib_json['records']:
        if int(i['fields']['dist']) < DMIN:
            DMIN = int(i['fields']['dist'])
            station_min = i['fields']['xy']
            adresse_station_min = i['fields']['adresse']
    return (station_min,adresse_station_min)