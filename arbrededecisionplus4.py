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
    reponse_transit = Reponse.reponse_transit(meta)
    reponse_walking = Reponse.reponse_walking(meta)
    reponse_velib = Reponse.reponse_velib(meta)

    if chargement=="beaucoup":
        print("Vous êtes chargés mais trop nombreux pour rentrer dans une autolib... Louez un petit van!")
    else:
        if meteo == "pluie" or temperature < 0:
            print(reponse_transit)
        else:
            if meteo == "soleil" and temperature > 15:
                if chargement == "un peu":
                    if meta.min_durationTW()[0] == "transit":
                        if meta.tauxdiff_durationWT()<0.15 and meta.diff_durationWT()<600:
                            print(reponse_walking)
                        else:
                            print(reponse_transit)
                    else:
                        print(reponse_walking)
                else:
                    if meta.min_durationTVW()[0] == "velib":
                        print(reponse_velib)
                    elif meta.min_durationTVW()[0] == "walking":
                        print(reponse_walking)
                    else:
                        if meta.min_durationVW()[0] == "velib":
                            if meta.tauxdiff_durationVT() <0.15 and meta.diff_durationVT()<600:
                                print(reponse_velib)
                            else:
                                print(reponse_transit)
                        else:
                            if meta.tauxdiff_durationWT() < 0.15 and meta.diff_durationWT()<600:
                                print(reponse_walking)
                            else:
                                print(reponse_transit)
            else:
                if chargement == "un peu":
                    if meta.walking_duration > 1500:
                        print(reponse_transit)
                    else:
                        if meta.min_durationTW() == "walking":
                            print(reponse_walking)
                        else:
                            print(reponse_transit)
                else:
                    if meta.walking_duration > 1500:
                        if meta.min_durationTV()[0] == "transit":
                            print(reponse_transit)
                        else:
                            print(reponse_velib)
                    else:
                        if meta.min_durationTVW()[0]=="velib":
                            print(reponse_velib)
                        elif meta.min_durationTVW()[0]=="walking":
                            print(reponse_walking)
                        else:
                            print(reponse_transit)