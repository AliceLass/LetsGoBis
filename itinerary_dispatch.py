# -*-coding:Utf-8 -*

'''Module créant les classes d'itineraires associes a chacun des moyens de transport'''

import itinerary
import velib
import autolib
import point

class ItineraryAutolib:
    '''Classe qui permet le dispatch des itineraires des etapes pour l'autolib'''

    def __init__(self, origin, arrival):
        '''Constructeur de la classe ItineraryAutolib'''
        self.origin=origin
        self.arrival=arrival
        self.station_origin = point.Point()
        self.station_origin.from_coord(autolib.autolib(origin)[0])
        self.station_arrival = point.Point()
        self.station_arrival.from_coord(autolib.autolib(arrival)[0])
        # On crée les 3 itineraires
        self.walk_to_station = itinerary.Itinerary(origin, self.station_origin, 'walking')
        self.driving = itinerary.Itinerary(self.station_origin, self.station_arrival, 'driving')
        self.walk_to_arrival = itinerary.Itinerary(self.station_arrival, arrival, 'walking')
        self.walking_duration = self.walk_to_station.duration + self.walk_to_arrival.duration
        self.duration = self.walk_to_station.duration + self.driving.duration + self.walk_to_arrival.duration

    def dispatch_duration(self):
        '''Methode qui envoie le dispatch des temps de transit sous forme d'une liste'''
        walking1 = self.walk_to_station.duration
        walking1 = walking1 // 60
        walking2 = self.walk_to_arrival.duration
        walking2 = walking2 // 60
        drive_duration = self.driving.duration
        drive_duration = drive_duration // 60
        return [walking1, drive_duration, walking2]


class ItineraryVelib:
    '''Classe qui permet le dispatch des itineraires des etapes pour le velib'''

    def __init__(self, origin, arrival):
        '''Constructeur de la classe'''
        self.origin = origin
        self.arrival = arrival
        self.station_origin = point.Point()
        self.station_origin.from_coord(velib.velib(origin)[0])
        self.station_arrival = point.Point()
        self.station_arrival.from_coord(velib.velib(arrival)[0])
        # On crée les 3 itineraires
        self.walk_to_station = itinerary.Itinerary(origin, self.station_origin, 'walking')
        self.biking = itinerary.Itinerary(self.station_origin, self.station_arrival, 'bicycling')
        self.walk_to_arrival = itinerary.Itinerary(self.station_arrival, arrival, 'walking')
        self.walking_duration = self.walk_to_station.duration + self.walk_to_arrival.duration
        self.duration = self.walk_to_station.duration + self.biking.duration + self.walk_to_arrival.duration

    def dispatch_duration(self):
        '''Methode qui envoie le dispatch des temps de transit sous forme d'une liste'''
        walking1 = self.walk_to_station.duration
        walking1 = walking1 // 60
        walking2 = self.walk_to_arrival.duration
        walking2 = walking2 // 60
        bike_duration = self.biking.duration
        bike_duration = bike_duration // 60
        return [walking1, bike_duration, walking2]


class ItineraryWalk:
    '''Classe qui permet le dispatch des itineraires des etapes pour la marche'''

    def __init__(self, origin, arrival):
        '''Constructeur de classe'''
        self.origin = origin
        self.arrival = arrival
        self.walk_to_arrival = itinerary.Itinerary(origin, arrival, 'walking')
        self.walking_duration = self.walk_to_arrival.duration
        self.duration = self.walk_to_arrival.duration

    def dispatch_duration(self):
        '''Methode qui envoie le dispatch des temps de transit sous forme d'une liste'''
        walking1 = self.walk_to_arrival.duration
        walking1 = walking1 // 60
        return [walking1]


class ItineraryTransit:
    '''Classe qui permet le dispatch des itineraires des etapes pour les transports en commun'''

    def __init__(self, origin, arrival):
        '''Constructeur de la classe ItineraryTransit'''
        self.origin = origin
        self.arrival = arrival
        self.steps = itinerary.Itinerary(origin, arrival, 'transit').itinerary["routes"][0]["legs"][0]["steps"]
        self.walking_duration = 0
        self.transit_duration = 0
        self.nb_liaisons = -1
        for i in self.steps:
            if i["travel_mode"] == "WALKING":
                self.walking_duration += int(i["duration"]["value"])
            elif i["travel_mode"] == "TRANSIT":
                self.transit_duration += int(i["duration"]["value"])
                self.nb_liaisons += 1
        self.duration = self.transit_duration+self.walking_duration

    def dispatch_duration(self):
        '''Methode qui envoie le dispatch des temps de transit sous forme d'une liste'''
        return ([self.walking_duration // 60, self.transit_duration // 60])

    def itinerary_steps(self):
        '''Methode qui retourne une liste de dictionnaires avec les informations de chaque etape du transport'''
        steps = []
        for i in self.steps:
            if i['travel_mode'] == "TRANSIT":
                step = {}
                step['departure_stop'] = i['transit_details']['departure_stop']['name']
                step['line'] = i['transit_details']['line']['short_name']
                step['direction'] = i['transit_details']['headsign']
                step['type'] = i['transit_details']['line']['vehicle']['name']
                step['arrival_stop'] = i['transit_details']['arrival_stop']['name']
                steps.append(step)
        return steps
