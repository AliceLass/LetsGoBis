# -*-coding:Utf-8 -*

import geopy
from geopy.geocoders import Nominatim

class Point:
    '''Classe contenant les coordonnées des points'''

    def __init__(self):
        '''Constructeur de classe'''
        self.location=""
        self.address=""
        self.latitude=""
        self.longitude=""
        self.coordinates=""
		
    def from_address(self, address): #prend en entrée une adresse au format n° rue Ville.
        '''Methode de classe permettant de remplir un point avec une adresse en entrée'''
        geolocator=Nominatim()
        self.location=geolocator.geocode(str(address))
        self.address=self.location.address
        self.latitude=self.location.latitude
        self.longitude=self.location.longitude
        self.coordinates=(self.latitude,self.longitude)

    def from_coord(self, coord): #prend en entrée une liste de coordonée au format [x,y]"
        '''Methode de classe permettant de remplir un point avec des coordonées en entrée'''
        geolocator=Nominatim()
        self.location=geolocator.reverse(str(coord).strip('[]'))
        self.address=self.location.address
        self.latitude=self.location.latitude
        self.longitude=self.location.longitude
        self.coordinates=(self.latitude,self.longitude)

    def print_coordinates(self):
        '''Methode renvoyant les coordonnées d'une adresse'''
        return((self.latitude,self.longitude))

    def dist_to_coordinates(self, dist):
        '''Methode renvoyant les coordonnees d'un point et une distance'''
        return((self.latitude,self.longitude,dist))

    def __repr__(self):
        '''Methode de representation'''
        return (self.address)
	
