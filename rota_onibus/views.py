from django.shortcuts import render
from folium import Map, Marker, Popup
from folium.features import CustomIcon
import folium

def rota_onibus(request):
    m = Map(location=[-10.436857, -45.167572], zoom_start=16)


    folium.PolyLine(locations=[[-10.43029, -45.174006],
                               [-10.438233, -45.173019],
                               [-10.454374, -45.171460],
                               [-10.439672, -45.168913],
                               [-10.443239, -45.160735],
                               [-10.445821973840223, -45.157225573894166],
                               [-10.451489284715427, -45.14632978025354],
                               [-10.454766, -45.137556]],
                    color='blue', weight=5, opacity=1).add_to(m)

    folium.PolyLine(locations=[[-10.454766, -45.137556],
                               [-10.451376, -45.146146],
                               [-10.445506, -45.157068],
                               [-10.436312209746829, -45.16206752940275],
                               [-10.429963618789197, -45.16191090829542],
                               [-10.43029, -45.174006]],
                    color='red', weight=5, opacity=1).add_to(m)

    for local in [{"location": [-10.43029, -45.174006], "popup": "IFPI - Campus Corrente"},
                  {"location": [-10.438233, -45.173019], "popup": "Posto de Combustível Primavera"},
                  {"location": [-10.454374, -45.171460], "popup": "Praça Principal do Vermelhão"},
                  {"location": [-10.439672, -45.168913], "popup": "Supermercado Rocha"},
                  {"location": [-10.443239, -45.160735], "popup": "Praça da Igreja Batista"},
                  {"location": [-10.445821973840223, -45.157225573894166], "popup": "15ª Regional de Educação"},
                  {"location": [-10.451489284715427, -45.14632978025354], "popup": "Posto de Combustível do Aeroporto"},
                  {"location": [-10.454766, -45.137556], "popup": "Escola Municipal Orley Cavalcante Pacheco"},
                  
                  
                  {"location": [-10.445506, -45.157068], "popup": "15ª Regional de Educação"},
                  {"location": [-10.451376, -45.146146], "popup": "APAE"},
                  {"location": [-10.445506, -45.157068], "popup": "SAMU"},
                  {"location": [-10.436312209746829, -45.16206752940275], "popup": "Caixa d'Água"},
                  {"location": [-10.429963618789197, -45.16191090829542], "popup": "Trevo da Entrada do Morro do Pequi"},
                  {"location": [-10.43029, -45.174006], "popup": "IFPI - Campus Corrente"},
                  ]:
        icon_bus_stop = CustomIcon(icon_image='bus.png',
                                   icon_size=(30, 30))
        Marker(location=local["location"], icon=icon_bus_stop, popup=Popup(local["popup"])).add_to(m)

    return render(request, 'rota_onibus.html', {'map': m._repr_html_()})
