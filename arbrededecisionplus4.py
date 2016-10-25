# -*-coding:Utf-8 -*

import MetaItinerary
import Meteo
import Reponse

def arbreplus4(origin, arrival, chargement):
    ''' Fonction d'arbre de decision si il y a plus de 4 passagers '''

    # Infos sur les passagers
    meta = MetaItinerary.MetaItinerary(origin, arrival)

    # Infos depuis API
    meteo = Meteo.meteo()[1]
    temperature = Meteo.meteo()[0]
    reponse_transit = Reponse.reponse_transit()
    reponse_walking = Reponse.reponse_walking()
    reponse_velib = Reponse.reponse_velib()

    if chargement=="beaucoup":
        print("Vous êtes chargés mais trop nombreux pour rentrer dans une autolib... Louez un petit van!")
    else:
        if meteo == "pluie" or temperature < 0:
            return reponse_transit
        else:
            if meteo == "soleil" and temperature > 15:
                if chargement == "un peu":
                    if meta.min_durationTW()[0] == "transit":
                        if meta.tauxdiff_durationWT()<0.15 and meta.diff_durationWT()<600:
                            return reponse_walking
                        else:
                            return reponse_transit
                    else:
                        return reponse_walking
                else:
                    if meta.min_durationTVW()[0] == "velib":
                        return reponse_velib
                    elif meta.min_durationTVW()[0] == "walking":
                        return reponse_walking
                    else:
                        if meta.min_durationVW()[0] == "velib":
                            if meta.tauxdiff_durationVT() <0.15 and meta.diff_durationVT()<600:
                                return reponse_velib
                            else:
                                return reponse_transit
                        else:
                            if meta.tauxdiff_durationWT() < 0.15 and meta.diff_durationWT()<600:
                                return reponse_walking
                            else:
                                return reponse_transit
            else:
                if chargement == "un peu":
                    if meta.walking_duration > 1500:
                        return reponse_transit
                    else:
                        if meta.min_durationTW() == "walking":
                            return reponse_walking
                        else:
                            return reponse_transit
                else:
                    if meta.walking_duration > 1500:
                        if meta.min_durationTV()[0] == "transit":
                            return reponse_transit
                        else:
                            return reponse_velib
                    else:
                        if meta.min_durationTVW()[0]=="velib":
                            return reponse_velib
                        elif meta.min_durationTVW()[0]=="walking":
                            return reponse_walking
                        else:
                            return reponse_transit