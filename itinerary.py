# -*-coding:Utf-8 -*

'''Module permettant de créer un itineraire entre un point de depart et un point d'arrivee avec un mode de transport defini'''
import requests

API_gglekey="AIzaSyBsakgF5UCvejwmCE0t5y0pFCdk7AACIy8"

class Itinerary:
	'''Classe destinée a stocker un itineraire appelé sur l'API google maps'''

	def __init__(self, origin, arrival, mode): #mode doit prendre une valeur dans walking, driving, bicycling, transit
		'''Constructeur de la classe Itinerary'''
		or_coord=origin.coordinates
		ar_coord=arrival.coordinates

		#On prefere garder l'URL séparée afin de la modifier facilement
		URL="https://maps.googleapis.com/maps/api/directions/json?origin="+str(or_coord[0])+","+str(or_coord[1])+"&destination="+str(ar_coord[0])+","+str(ar_coord[1])+"&mode="+mode+"&key="+API_gglekey
		r=requests.get(URL)
		if r.status_code != 200:
			print("La requete a echoué")
		else :		
			self.itinerary=r.json()
			self.duration=int(self.itinerary["routes"][0]["legs"][0]["duration"]["value"])
	

