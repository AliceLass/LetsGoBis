"""Module permettant de donner la météo de Paris"""

import requests
import json
import pprint

#Création de l'URL de l'API
def _url():
    chaine='http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=40c9d46000b38d74cb542be743bf857d'
    return chaine

#Retourne le JSON avec les paramètres météo
def get_meteo():
    return requests.get(_url())

#Retourne les variables meteo et temperature
def meteo():
    meteo=''
    if get_meteo().json()['weather'][0]['main']=="Clouds":
        meteo='moyen'
    if get_meteo().json()['weather'][0]['main']=="Clear":
        meteo='soleil'
    else:
        meteo='pluie'
    temp_k = int((get_meteo().json()['main']['temp']))
    temperature = temp_k - 273.15
    return [temperature,meteo]

print(meteo())

