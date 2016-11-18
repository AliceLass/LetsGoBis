# -*-coding:Utf-8 -*

"""Module permettant de donner la météo de Paris"""

import requests

def _url():
    '''Fonction qui crée l'URL de l'API'''
    chaine='http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=40c9d46000b38d74cb542be743bf857d'
    return chaine

def get_meteo():
    '''Fonction qui retourne le JSON avec les paramètres météo'''
    return requests.get(_url())

def meteo():
    '''Fonction qui retourne les variables temps et temperature'''
    temps=''
    if get_meteo().json()['weather'][0]['main']=="Clouds":
        temps='moyen'
    if get_meteo().json()['weather'][0]['main']=="Clear":
        temps='soleil'
    else:
        temps='pluie'
    temp_k = int((get_meteo().json()['main']['temp']))
    temperature = temp_k - 273.15
    return [temperature,temps]

