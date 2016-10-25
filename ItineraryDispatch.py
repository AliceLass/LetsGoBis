# -*-coding:Utf-8 -*

import Itinerary
import velib
import autolib
import Point

#L'objectif est de creer des class séparées pour chaque type d'itineraire.

class ItineraryAutolib:
    #Dispatch des itineraires des etapes pour l'autolib.
    def __init__(self, Origin, Arrival):
        # On definit les points intermediaires
        self.Origin=Origin
        self.Arrival=Arrival
        self.StationOrigin = Point.Point()
        self.StationOrigin.FromCoord(autolib.autolib(Origin)[0])
        self.StationArrival = Point.Point()
        self.StationArrival.FromCoord(autolib.autolib(Arrival)[0])
        # On crée les 3 itineraires
        self.WalkToStation = Itinerary.Itinerary(Origin, self.StationOrigin, 'walking')
        self.Driving = Itinerary.Itinerary(self.StationOrigin, self.StationArrival, 'driving')
        self.WalkToArrival = Itinerary.Itinerary(self.StationArrival, Arrival, 'walking')
        self.walking_duration = self.WalkToStation.duration + self.WalkToArrival.duration
        self.duration = self.WalkToStation.duration + self.Driving.duration + self.WalkToArrival.duration

    def DispatchDuration(self):
        # envoie le dispatch des temps de transit sous forme d'une liste.
        Walking1 = self.WalkToStation.duration
        Walking1 = Walking1 // 60
        Walking2 = self.WalkToArrival.duration
        Walking2 = Walking2 // 60
        DriveDuration = self.Driving.duration
        DriveDuration = DriveDuration // 60
        return [Walking1, DriveDuration, Walking2]


class ItineraryVelib:
    # Dispatch des itineraires des etapes pour le velib.
    def __init__(self, Origin, Arrival):
        # On definit les points intermediaires
        self.Origin = Origin
        self.Arrival = Arrival
        self.StationOrigin = Point.Point()
        self.StationOrigin.FromCoord(velib.velib(Origin)[0])
        self.StationArrival = Point.Point()
        self.StationArrival.FromCoord(velib.velib(Arrival)[0])
        # On crée les 3 itineraires
        self.WalkToStation = Itinerary.Itinerary(Origin, self.StationOrigin, 'walking')
        self.Biking = Itinerary.Itinerary(self.StationOrigin, self.StationArrival, 'bicycling')
        self.WalkToArrival = Itinerary.Itinerary(self.StationArrival, Arrival, 'walking')
        self.walking_duration = self.WalkToStation.duration + self.WalkToArrival.duration
        self.duration = self.WalkToStation.duration + self.Biking.duration + self.WalkToArrival.duration

    def DispatchDuration(self):
        # envoie le dispatch des temps de transit sous forme d'une liste.
        Walking1 = self.WalkToStation.duration
        Walking1 = Walking1 // 60
        Walking2 = self.WalkToArrival.duration
        Walking2 = Walking2 // 60
        BikeDuration = self.Biking.duration
        BikeDuration = BikeDuration // 60
        return [Walking1, BikeDuration, Walking2]


class ItineraryWalk:
    # Itineraire simple pour la marche.
    def __init__(self, Origin, Arrival):
        self.Origin = Origin
        self.Arrival = Arrival
        self.WalkToArrival = Itinerary.Itinerary(Origin, Arrival, 'walking')
        self.walking_duration = self.WalkToArrival.duration
        self.duration = self.WalkToArrival.duration

    def DispatchDuration(self):
        # envoie le dispatch des temps de transit sous forme d'une liste.
        Walking1 = self.WalkToStation.duration
        Walking1 = Walking1 // 60
        return [Walking1]


class ItineraryTransit:
    def __init__(self, Origin, Arrival):
        self.Origin = Origin
        self.Arrival = Arrival
        self.steps = Itinerary.Itinerary(Origin, Arrival, 'transit').itinerary["routes"][0]["legs"][0]["steps"]
        self.walking_duration = 0
        self.transit_duration = 0
        self.nb_liaisons = -1
        for i in self.steps:
            if i["travel_mode"] == "WALKING":
                self.walking_duration += int(i["duration"]["value"])
            elif i["travel_mode"] == "TRANSIT":
                self.transit_duration += int(i["duration"]["value"])
                self.nb_liaisons += 1
        self.duration = self.Transit.duration

    def DispatchDuration(self):
        # envoie le dispatch des temps de transit sous forme d'une liste.
        return ([self.walking_duration // 60, self.transit_duration // 60])

    def ItinerarySteps(self):
        #Construire une liste de dictionnaire avec les informations de chaques etapes du transport
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
