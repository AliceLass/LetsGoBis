# -*-coding:Utf-8 -*

"""Module permettant de trouver la station autolib la plus proche en prenant en entrée un pointde la classe Point"""

import requests

def _url(point):
    '''Fonction créant l'URL avec les coordonnées GPS long,lat et une distance D'''
    D = 500
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&facet=banking&facet=bonus&facet=status&facet=contract_name&geofilter.distance='+str(point.latitude)+'%2C+'+str(point.longitude)+'%2C'+str(D)
    return chaine


def get_velib(point):
    '''Fonction qui retourne le JSON avec les stations autolib correspondant à URL'''
    return requests.get(_url(point))


def velib(point):
    '''Fonction qui va chercher la station la plus proche et ses coordonnées dans le JSON'''
    velib_json=get_velib(point).json()
    DMIN = 500
    station_min = []
    adress_station_min=""

    for i in velib_json['records']:
        if int(i['fields']['dist']) < DMIN:
            DMIN = int(i['fields']['dist'])
            station_min = i['fields']['position']
            adress_station_min = i['fields']['address']
    return (station_min,adress_station_min)