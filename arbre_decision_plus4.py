# -*-coding:Utf-8 -*

'''Module contenant l'arbre de decision dans le cas ou il y a plus de 4 passagers (l'option autolib est mise de cote)'''

import meta_itinerary
import meteo
import reponse

def arbre_plus4(origin, arrival, chargement):
    ''' Fonction d'arbre de decision si il y a plus de 4 passagers '''

    # Infos sur les passagers
    meta = meta_itinerary.MetaItinerary(origin, arrival)

    # Infos depuis API
    temps = meteo.meteo()[1]
    temperature = meteo.meteo()[0]
    reponse_transit = reponse.reponse_transit(meta)
    reponse_walking = reponse.reponse_walking(meta)
    reponse_velib = reponse.reponse_velib(meta)

    if chargement=="beaucoup":
        print("Vous êtes chargés mais trop nombreux pour rentrer dans une autolib... Louez un petit van!")
    else:
        if temps == "pluie" or temperature < 0:
            print(reponse_transit)
        else:
            if temps == "soleil" and temperature > 15:
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