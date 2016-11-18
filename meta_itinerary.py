# -*-coding:Utf-8 -*

'''Module qui crée des fonctions determinantes dans les arbres de decision (moins4 et plus4)'''

import itinerary_dispatch

class MetaItinerary:
    '''Classe de jeux d'itineraires'''

    def __init__(self, origin, arrival):
        '''Constructeur de la classe'''
        self.origin = origin
        self.arrival = arrival
        self.walkingitinerary = itinerary_dispatch.ItineraryWalk(self.origin, self.arrival)
        self.velibitinerary = itinerary_dispatch.ItineraryVelib(self.origin, self.arrival)
        self.autolibitinerary = itinerary_dispatch.ItineraryAutolib(self.origin, self.arrival)
        self.transititinerary = itinerary_dispatch.ItineraryTransit(self.origin, self.arrival)
        self.walking_duration = self.walkingitinerary.duration
        self.walking_walkingduration = self.walkingitinerary.walking_duration
        self.velib_duration=self.velibitinerary.duration
        self.velib_walkingduration = self.velibitinerary.walking_duration
        self.autolib_duration = self.autolibitinerary.duration
        self.autolib_walkingduration = self.autolibitinerary.walking_duration
        self.transit_duration = self.transititinerary.duration
        self.transit_walkingduration = self.transititinerary.walking_duration


    def min_durationAT(self):
        '''Methode qui renvoie le durée totale minimum entre l'Autolib et le Transit'''
        result=[]
        if min(self.autolib_duration, self.transit_duration)==self.autolib_duration:
            result.append("autolib")
        else:
            result.append("transit")
        result.append(min(self.autolib_duration, self.transit_duration))
        return result

    def min_durationATV(self):
        '''Methode qui renvoie le durée totale minimum entre l'Autolib, le Transit et le Velib'''
        result = []
        if min(self.autolib_duration, self.transit_duration, self.velib_duration) == self.autolib_duration:
            result.append("autolib")
        elif min(self.autolib_duration, self.transit_duration, self.velib_duration) == self.transit_duration:
            result.append("transit")
        else :
            result.append("velib")
        result.append(min(self.autolib_duration, self.transit_duration, self.velib_duration))
        return result

    def min_durationATVW(self):
        '''Methode qui renvoie le durée totale minimum entre les quatre moyens de transport'''
        result = []
        if min(self.autolib_duration, self.transit_duration, self.velib_duration, self.walking_duration) == self.autolib_duration:
            result.append("autolib")
        elif min(self.autolib_duration, self.transit_duration, self.velib_duration, self.walking_duration) == self.transit_duration:
            result.append("transit")
        elif min(self.autolib_duration, self.transit_duration, self.velib_duration, self.walking_duration) == self.velib_duration:
            result.append("velib")
        else:
            result.append("walking")
        result.append(min(self.autolib_duration, self.transit_duration, self.velib_duration, self.walking_duration))
        return result

    def min_durationATW(self):
        '''Methode qui renvoie le durée totale minimum entre l'Autolib, le Transit et le Walking'''
        result = []
        if min(self.autolib_duration, self.transit_duration, self.walking_duration) == self.autolib_duration:
            result.append("autolib")
        elif min(self.autolib_duration, self.transit_duration, self.walking_duration) == self.transit_duration:
            result.append("transit")
        else:
            result.append("walking")
        result.append(min(self.autolib_duration, self.transit_duration, self.walking_duration))
        return result

    def min_durationTV(self):
        '''Methode qui renvoie le durée totale minimum entre le Transit et le Velib'''
        result = []
        if min(self.transit_duration, self.velib_duration) == self.transit_duration:
            result.append("transit")
        else:
            result.append("velib")
        result.append(min(self.transit_duration, self.velib_duration))
        return result

    def min_durationTW(self):
        '''Methode qui renvoie le durée totale minimum entre le Transit et le Walking'''
        result = []
        if min(self.transit_duration, self.walking_duration) == self.transit_duration:
            result.append("transit")
        else:
            result.append("walking")
        result.append(min(self.transit_duration, self.walking_duration))
        return result

    def min_durationTVW(self):
        '''Methode qui renvoie le durée totale minimum entre le Transit, le Velib et le Walking'''
        result = []
        if min(self.transit_duration, self.velib_duration, self.walking_duration) == self.transit_duration:
            result.append("transit")
        elif min(self.transit_duration, self.velib_duration, self.walking_duration) == self.velib_duration:
            result.append("velib")
        else:
            result.append("walking")
        result.append(min(self.transit_duration, self.velib_duration, self.walking_duration))
        return result

    def min_durationVW(self):
        '''Methode qui renvoie le durée totale minimum entre le Velib et le Walking'''
        result = []
        if min(self.velib_duration, self.walking_duration) == self.velib_duration:
            result.append("velib")
        else:
            result.append("walking")
        result.append(min(self.velib_duration, self.walking_duration))
        return result



    def diff_walkingdurationAT(self):
        '''Methode qui renvoie la différence de durée de marche entre Autolib et Transit'''
        return self.autolib_walkingduration - self.transit_walkingduration

    def diff_walkingdurationTA(self):
        '''Methode qui renvoie la différence de durée de marche entre Transit et Autolib'''
        return self.transit_walkingduration - self.autolib_walkingduration



    def diff_durationVA(self):
        '''Methode qui renvoie la différence de durée totale entre Velib et Autolib'''
        return self.velib_duration - self.autolib_duration

    def diff_durationVT(self):
        '''Methode qui renvoie la différence de durée totale entre Velib et Transit'''
        return self.velib_duration - self.transit_duration

    def diff_durationWA(self):
        '''Methode qui renvoie la différence de durée totale entre Walking et Autolib'''
        return self.walking_duration - self.autolib_duration

    def diff_durationWT(self):
        '''Methode qui renvoie la différence de durée totale entre Walking et Transit'''
        return self.walking_duration - self.transit_duration

    def diff_durationAT(self):
        '''Methode qui renvoie la différence de durée totale entre Autolib et Transit'''
        return self.autolib_duration - self.transit_duration



    def tauxdiff_durationVA(self):
        '''Methode qui renvoie le taux de rallongement de la durée du trajet en choisissant Velib par rapport à Autolib'''
        return self.diff_durationVA() / self.autolib_duration

    def tauxdiff_durationVT(self):
        '''Methode qui renvoie le taux de rallongement de la durée du trajet en choisissant Velib par rapport à Transit'''
        return self.diff_durationVT() / self.transit_duration

    def tauxdiff_durationWA(self):
        '''Methode qui renvoie le taux de rallongement de la durée du trajet en choisissant Walking par rapport à Autolib'''
        return self.diff_durationWA() / self.autolib_duration

    def tauxdiff_durationWT(self):
        '''Methode qui renvoie le taux de rallongement de la durée du trajet en choisissant Walking par rapport à Transit'''
        return self.diff_durationWT() / self.transit_duration

    def tauxdiff_durationTA(self):
        '''Methode qui renvoie le taux de rallongement de la durée du trajet en choisissant Transit par rapport à Autolib'''
        return (-1*self.diff_durationAT()) / self.autolib_duration

    def tauxdiff_durationAT(self):
        '''Methode qui renvoie le taux de rallongement de la durée du trajet en choisissant Autolib par rapport à Transit'''
        return self.diff_durationAT() / self.transit_duration

