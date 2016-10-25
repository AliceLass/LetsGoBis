# -*-coding:Utf-8 -*

"""Module permettant de trouver la station autolib la plus proche en prenant en entrée un pointde la classe Point"""

import requests

#Créer l'URL avec les coordonnées GPS long,lat et une distance d
def _url(point):
    d=500
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations_et_espaces_autolib_de_la_metropole_parisienne&facet=ville&facet=type&facet=cp&refine.ville=Paris&geofilter.distance='+str(point.latitude)+'%2C+'+str(point.longitude)+'%2C'+str(d)
    return chaine

#Retourne le JSON avec les stations autolib correspondant à URL
def get_autolib(point):
    return requests.get(_url(point))

def autolib(point):
    autolib_json=get_autolib(point).json()
    dmin = 500
    station_min = []
    adresse_station_min=""

    for i in autolib_json['records']:
        if int(i['fields']['dist']) < dmin:
            dmin = int(i['fields']['dist'])
            station_min = i['fields']['xy']
            adresse_station_min = i['fields']['adresse']
    return (station_min,adresse_station_min)