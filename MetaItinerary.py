# -*-coding:Utf-8 -*

import ItineraryDispatch
import Exemple


class MetaItinerary:

    def __init__(self, origin, arrival):
        self.origin = origin
        self.arrival = arrival
        self.walkingitinerary = ItineraryDispatch.ItineraryWalk(self.origin, self.arrival)
        self.velibitinerary = ItineraryDispatch.ItineraryVelib(self.origin, self.arrival)
        self.autolibitinerary = ItineraryDispatch.ItineraryAutolib(self.origin, self.arrival)
        self.transititinerary = ItineraryDispatch.ItineraryTransit(self.origin, self.arrival)
        self.walking_duration = self.walkingitinerary.duration
        self.walking_walkingduration = self.walkingitinerary.walking_duration
        self.velib_duration=self.velibitinerary.duration
        self.velib_walkingduration = self.velibitinerary.walking_duration
        self.autolib_duration = self.autolibitinerary.duration
        self.autolib_walkingduration = self.autolibitinerary.walking_duration
        self.transit_duration = self.transititinerary.duration
        self.transit_walkingduration = self.transititinerary.walking_duration
    # Methodes de la classe MetaItinerary qui renvoient la durée totale minimum entre différents moyens de transport

    def min_durationAT(self):
        # Méthode qui renvoie le durée totale minimum entre l'Autolib et le Transit
        result=[]
        if min(self.autolib_duration, self.transit_duration)==self.autolib_duration:
            result.append("autolib")
        else:
            result.append("transit")
        result.append(min(self.autolib_duration, self.transit_duration))
        return result

    def min_durationATV(self):
        # Méthode qui renvoie le durée totale minimum entre l'Autolib, le Transit et le Velib
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
        # Méthode qui renvoie le durée totale minimum entre les quatre moyens de transport
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
        # Méthode qui renvoie le durée totale minimum entre l'Autolib, le Transit et le Walking
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
        # Méthode qui renvoie le durée totale minimum entre le Transit et le Velib
        result = []
        if min(self.transit_duration, self.velib_duration) == self.transit_duration:
            result.append("transit")
        else:
            result.append("velib")
        result.append(min(self.transit_duration, self.velib_duration))
        return result

    def min_durationTW(self):
        # Méthode qui renvoie le durée totale minimum entre le Transit et le Walking
        result = []
        if min(self.transit_duration, self.walking_duration) == self.transit_duration:
            result.append("transit")
        else:
            result.append("walking")
        result.append(min(self.transit_duration, self.walking_duration))
        return result

    def min_durationTVW(self):
        # Méthode qui renvoie le durée totale minimum entre le Transit, le Velib et le Walking
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
        # Méthode qui renvoie le durée totale minimum entre le Velib et le Walking
        result = []
        if min(self.velib_duration, self.walking_duration) == self.velib_duration:
            result.append("velib")
        else:
            result.append("walking")
        result.append(min(self.velib_duration, self.walking_duration))
        return result


    # Methodes de la classe MetaItinerary qui renvoient la différence de durée de marche entre deux moyens de transports

    def diff_walkingdurationAT(self):
        return self.autolib_walkingduration - self.transit_walkingduration

    def diff_walkingdurationTA(self):
        return self.transit_walkingduration - self.autolib_walkingduration


    # Methodes de la classe MetaItinerary qui renvoient la différence de durée totale entre deux moyens de transports

    def diff_durationVA(self):
        return self.velib_duration - self.autolib_duration

    def diff_durationVT(self):
        return self.velib_duration - self.transit_duration

    def diff_durationWA(self):
        return self.walking_duration - self.autolib_duration

    def diff_durationWT(self):
        return self.walking_duration - self.transit_duration

    def diff_durationAT(self):
        return self.autolib_duration - self.transit_duration




    # Methodes de la classe MetaItinerary qui renvoient le taux de rallongement de la durée du trajet en choisissant I par rapport à J

    def tauxdiff_durationVA(self):
        return self.diff_durationVA() / self.autolib_duration

    def tauxdiff_durationVT(self):
        return self.diff_durationVT() / self.transit_duration

    def tauxdiff_durationWA(self):
        return self.diff_durationWA() / self.autolib_duration

    def tauxdiff_durationWT(self):
        return self.diff_durationWT() / self.transit_duration

testMetaItinerary = MetaItinerary(Exemple.OriginExemple, Exemple.ArrivalExemple)
print(testMetaItinerary.tauxdiff_durationWA())

