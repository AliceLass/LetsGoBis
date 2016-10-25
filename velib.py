# -*-coding:Utf-8 -*

"""Module permettant de trouver la station autolib la plus proche en prenant en entrée un pointde la classe Point"""

import requests

#Créer l'URL avec les coordonnées GPS long,lat et une distance d
def _url(point):
    chaine='http://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&facet=banking&facet=bonus&facet=status&facet=contract_name&geofilter.distance='+str(point.latitude)+'%2C+'+str(point.longitude)+'%2C'+str(d)

    return chaine

#Retourne le JSON avec les stations autolib correspondant à URL
def get_velib(point):
    return requests.get(_url(point))

#Va chercher la station la plus proche et ses coordonnées dans le JSON
def velib(point):
    velib_json=get_velib(point).json()
    dmin = 500
    station_min = []
    adress_station_min=""

    for i in velib_json['records']:
        if int(i['fields']['dist']) < dmin:
            dmin = int(i['fields']['dist'])
            station_min = i['fields']['position']
            adress_station_min = i['fields']['address']

    return (station_min,adress_station_min)