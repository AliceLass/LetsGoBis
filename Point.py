# -*-coding:Utf-8 -*

import geopy
from geopy.geocoders import Nominatim

geolocator=Nominatim()

class Point:
#Classe contenant les coordonées des points
	def __init__(self):
		self.location=""
		self.address=""
		self.latitude=""
		self.longitude=""
		self.coordinates=""
		
	def FromAddress(self,address):
	#prend en entrée une adresse au format ## rue Ville.
	#Methode de classe permettant d'allimenter un point avec une adresse en entrée
		geolocator=Nominatim()
		self.location=geolocator.geocode(str(address))
		self.address=self.location.address
		self.latitude=self.location.latitude
		self.longitude=self.location.longitude
		self.coordinates=(self.latitude,self.longitude)
		
	def FromCoord(self,coord):
	#prend en entrée une liste de coordonée au format [x,y]"
    # Methode de classe permettant d'allimenter un point avec des coordonées en entrée

    geolocator=Nominatim()
		self.location=geolocator.reverse(str(coord).strip('[]'))
		self.address=self.location.address
		self.latitude=self.location.latitude
		self.longitude=self.location.longitude
		self.coordinates=(self.latitude,self.longitude)
		
	def printcoordinates(self):
		return((self.latitude,self.longitude))
	
	def disttocoordinates(self,dist):
		return((self.latitude,self.longitude,dist))
		
	def __repr__(self):
		return (self.address)

	
		

	
