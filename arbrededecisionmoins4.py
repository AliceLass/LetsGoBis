# -*-coding:Utf-8 -*

import MetaItinerary
import Meteo
import Reponse

def arbremoins4(origin, arrival, chargement):
    ''' Fonction d'arbre de decision si il y a moins de 4 passagers '''

    # Infos sur les passagers
    meta = MetaItinerary.MetaItinerary(origin, arrival)

    # Infos depuis API
    meteo = Meteo.meteo()[1]
    temperature = Meteo.meteo()[0]
    reponse_transit = Reponse.reponse_transit()
    reponse_walking = Reponse.reponse_walking()
    reponse_velib = Reponse.reponse_velib()
    reponse_autolib = Reponse.reponse_autolib()

    if chargement== "beaucoup":
        return reponse_autolib
    else :
        if meteo == "pluie":
            if meta.min_durationAT()[0]=="autolib":
                if meta.diff_walkingdurationAT() > 600 and meta.tauxdiff_durationTA() < 0.15:
                    return reponse_transit
                else:
                    return reponse_autolib
            else:
                if meta.diff_walkingdurationTA() > 600 and meta.tauxdiff_durationAT() < 0.15 :
                    return reponse_autolib
                else:
                    return reponse_transit
        else :
            if temperature < 0 :
                if meta.min_durationAT()[0] == "autolib":
                    if meta.diff_walkingdurationAT() > 600 and meta.tauxdiff_durationTA() < 0.15:
                        return reponse_transit
                    else:
                        return reponse_autolib
                else:
                    if meta.diff_walkingdurationTA() > 600 and meta.tauxdiff_durationAT() < 0.15:
                        return reponse_autolib
                    else:
                        return reponse_transit
            else:
                if meteo == "soleil" and temperature > 15 :
                    if chargement=="un peu":
                        if meta.min_durationATW()[0]=="walking":
                            return reponse_walking
                        elif meta.min_durationATW()[0]=="autolib":
                            if meta.tauxdiff_durationWA() < 0.15 and meta.diff_durationWA() < 600:
                                return reponse_walking
                            else:
                                return reponse_autolib
                        else:
                            if meta.tauxdiff_durationWT() < 0.15 and meta.diff_durationWT() < 600:
                                return reponse_walking
                            else:
                                return reponse_transit
                    else:
                        if meta.min_durationATVW()[0]=="velib":
                            return reponse_velib
                        elif meta.min_durationATVW()[0]=="walking":
                            return reponse_walking
                        elif meta.min_durationATVW()[0]=="transit":
                            if meta.min_durationVW()[0]=="velib":
                                if meta.tauxdiff_durationVT() < 0.15 and meta.diff_durationVT < 600:
                                    return reponse_velib
                                else:
                                    return reponse_transit
                            else:
                                if meta.tauxdiff_durationWT() <0.15 and meta.diff_durationWT() < 600:
                                    return reponse_walking
                                else:
                                    return reponse_transit
                        else:
                            if meta.min_durationVW()[0]=="velib":
                                if meta.tauxdiff_durationVA() < 0.15 and meta.diff_durationVA < 600:
                                    return reponse_velib
                                else:
                                    return reponse_autolib
                            else:
                                if meta.tauxdiff_durationWA() <0.15 and meta.diff_durationWA() < 600:
                                    return reponse_walking
                                else:
                                    return reponse_autolib
                else:
                    if chargement=="un peu":
                        if meta.walking_duration > 1500:
                            if meta.min_durationAT()[0] == "autolib":
                                return reponse_autolib
                            else:
                                return reponse_transit
                        else:
                            if meta.min_durationATW()[0] == "autolib":
                                return reponse_autolib
                            elif meta.min_durationATW()[0] == "walking":
                                return reponse_walking
                            else:
                                return reponse_transit
                    else:
                        if meta.walking_duration > 1500:
                            if meta.min_durationATV()[0] == "velib":
                                return reponse_velib
                            elif meta.min_durationATV()[0] == "autolib":
                                return reponse_autolib
                            else :
                                return reponse_transit
                        else:
                            if meta.min_durationATVW()[0] == "autolib":
                                return reponse_autolib
                            elif meta.min_durationATVW()[0] == "transit":
                                return reponse_transit
                            elif meta.min_durationATVW()[0] == "velib":
                                return reponse_velib
                            else:
                                return reponse_walking