# -*-coding:Utf-8 -*

import requests
import Point

API_gglekey="AIzaSyBsakgF5UCvejwmCE0t5y0pFCdk7AACIy8"

class Itinerary:
	#Classe destinée a stocker un itineraire appelé sur l'API google maps.
	#mode doit prendre une valeur dans walking, driving, bicycling, transit.
	def __init__(self,Origin,Arrival,mode):
		OrCoord=Origin.coordinates
		ArCoord=Arrival.coordinates
		#On prefere garder l'URL séparée afin de la modifier facilement
		URL="https://maps.googleapis.com/maps/api/directions/json?origin="+str(OrCoord[0])+","+str(OrCoord[1])+"&destination="+str(ArCoord[0])+","+str(ArCoord[1])+"&mode="+mode+"&key="+API_gglekey
		r=requests.get(URL)
		if r.status_code != 200:
			print("La requete a echoué")
		else :		
			self.itinerary=r.json()
			self.duration=int(self.itinerary["routes"][0]["legs"][0]["duration"]["value"])
	

