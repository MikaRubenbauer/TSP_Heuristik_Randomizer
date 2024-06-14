from graph import *
from random import randint, choices
import matplotlib.pyplot as plt #muss in Thonny einfach als Packet installiert werden -> matplotlib
import numpy as np

def naechste_permutation(L):
    # bestimme den maximalen Index i mit L[i] < L[i+1]
    i = len(L)-2
    gefunden = False
    while not gefunden:
        if i < 0:
            gefunden = True
        else:
            if L[i] < L[i+1]:
                gefunden = True
            else:
                i = i-1
    if i >= 0:
        # bestimme den maximalen Index j mit L[j] > L[i]
        j = i+1
        m = j
        while j < len(L)-1:
            j = j+1
            if L[j] > L[i]:
                m = j
        j = m
        # vertausche L[i] und L[j]
        h = L[i]
        L[i] = L[j]
        L[j] = h
        # kehre die Restliste ab Position i+1 um
        i = i+1
        j = len(L)-1
        while i < j:
            h = L[i]
            L[i] = L[j]
            L[j] = h
            i = i+1
            j = j-1
    else:
        # Liste ist absteigend sortiert
        # kehre Liste um
        i = 0
        j = len(L)-1
        while i < j:
            h = L[i]
            L[i] = L[j]
            L[j] = h
            i = i+1
            j = j-1
    return L

#Berechnet die Wahrscheinlichkeit für alle Knoten in der knotenRestListeNeu
def getWahrscheinlichkeitsverteilung(abstaende):
    wahrscheinlichkeitsverteilung = []
    summe = sum(abstaende)
    for element in abstaende:
        wahrscheinlichkeitsverteilung.append(element/summe)
    return wahrscheinlichkeitsverteilung

#Berechnet den Abstand von jedem Knoten zum aktuellenKnoten
def getAbstaende(aktuellerKnoten,knotenRestListeNeu,g):
    abstaende = []
    for knoten in knotenRestListeNeu:
        abstaende.append(round(float(g.getGewichtKante(aktuellerKnoten,knoten))))
    return abstaende


def minimaleRundreise(g, startKnoten):
    startRouteOhneStartKnoten = []
    for knoten in g.getAlleKnoten():
        if knoten != startKnoten:
            startRouteOhneStartKnoten = startRouteOhneStartKnoten + [knoten]
    startRoute = [startKnoten] + startRouteOhneStartKnoten + [startKnoten]
    routeOhneStartKnoten = startRouteOhneStartKnoten[:]
    route = startRoute
    minLaenge = laenge(g, route)
    minRoute = route
    endePermutationen = False
    while not endePermutationen:
        routeOhneStartKnoten = naechste_permutation(routeOhneStartKnoten)
        route = [startKnoten] + routeOhneStartKnoten + [startKnoten]
        if laenge(g, route) < minLaenge:
            minLaenge = laenge(g, route)
            minRoute = route
        endePermutationen = (routeOhneStartKnoten == startRouteOhneStartKnoten)
    return (minRoute, minLaenge)


def laenge(g, rundreise):
    weglaenge = 0
    anzahlKnoten = len(rundreise)
    i = 1
    while i < anzahlKnoten:
        weglaenge = weglaenge + float(g.getGewichtKante(rundreise[i-1], rundreise[i]))
        i = i+1
    return weglaenge

def rundreiseNaeherung(g, startKnoten):
    zaehler = 1
    route = [startKnoten]
    knotenRestListe = []
    print('Initialisierung Route:', route)
    
    for knoten in g.getAlleKnoten():
        if knoten != startKnoten:
            knotenRestListe = knotenRestListe + [knoten]
    print('Initialisierung knotenRestListe:', knotenRestListe, '\n')
    
    while knotenRestListe != []:
        aktuellerKnoten = route[len(route)-1]
        print('Runde', zaehler)
        print('aktueller Knoten:', aktuellerKnoten)
        
        
        #for knoten in knotenRestListe:
            #abstandKnoten = g.getGewichtKante(aktuellerKnoten, knoten)
            #print('Knoten', knoten, 'hat Abstand:', abstandKnoten)
        
        abstaende = getAbstaende(aktuellerKnoten, knotenRestListe,g)
        wv = getWahrscheinlichkeitsverteilung(abstaende)
        abstand = choices(abstaende,weights=wv)[0]
        zufaelligeStelle = abstaende.index(abstand)
        ausgewaehlterKnoten = knotenRestListe[zufaelligeStelle]
        route = route + [ausgewaehlterKnoten]
        print(g.getAlleKnoten())
        
        print('Der restliche Gesammtlänge ist: ', abstand)
        result = [(Knoten,Wahrscheinlichkeit) for Knoten, Wahrscheinlichkeit in zip(knotenRestListe,wv)]
        
        print('Die aktuelle Wahrscheinlichkeit für jede Stadt ist: ',result)
        print('aktuelle Restliste', knotenRestListe)
        print('zufällig ausgewählter Knoten:', ausgewaehlterKnoten)
        
        knotenRestListeNeu = []
        for knoten in knotenRestListe:
            if knoten != ausgewaehlterKnoten:
                knotenRestListeNeu = knotenRestListeNeu + [knoten]
        knotenRestListe = knotenRestListeNeu
        zaehler += 1
        print('aktuelle Route', route)
        result = [(Knoten,Wahrscheinlichkeit) for Knoten, Wahrscheinlichkeit in zip(knotenRestListe,wv)]
        print('Die aktuelle Wahrscheinlichkeit für jede Stadt ist: ',result)
        print('aktuelle Restliste', knotenRestListe)
        
        
        print()
        
    route = route + [startKnoten]
    laengeRoute = laenge(g, route)
    return (route, laengeRoute)





# Erzeugung des Graph-Objekts
g = GraphMitDaten()
# Erzeugung der Knoten und Kanten aus einer GraphML-Datei
datei = open("graph_eu_13.xml", "r")
xml_quelltext = datei.read()
g.graphmlToGraph(xml_quelltext)

# Test der Rundreise-Algorithmus

# Näherungsverfahren 1
print('Näherungslösung Zufall')
(minRoute, minLaenge) = rundreiseNaeherung(g, 'Bonn')
print('Ergebnis:')
print('Route:', minRoute)
print('Länge:', minLaenge)
print()

# exakte Lösung
'''
print('kürzeste Rundreise')
(minRoute, minLaenge) = minimaleRundreise(g, 'Bonn')
print('Route:', minRoute)
print('Länge:', minLaenge)
print('\n\n\n')
'''

print('13 Städte:')
g = GraphMitDaten()
# Erzeugung der Knoten und Kanten aus einer GraphML-Datei
datei = open("graph_eu_13.xml", "r")
xml_quelltext = datei.read()
g.graphmlToGraph(xml_quelltext)

# Test der Rundreise-Algorithmus
laengeEpisodes = 1

# Näherungsverfahren 1
print('Näherungslösung statistischer Zufall')
besteRoute = []
besteLaenge = float('inf')
xAchse = []
listeBesteLaenge = []
listeAktuelleLaenge = []
for i in range(1,10):
    (minRoute, minLaenge) = rundreiseNaeherung(g, 'Bonn')
    if minLaenge <= besteLaenge:
        besteRoute = minRoute
        besteLaenge = minLaenge
    if i % laengeEpisodes == 0:   
        xAchse.append(i)
        listeBesteLaenge.append(besteLaenge)
        listeAktuelleLaenge.append(minLaenge)
   
    
print('Ergebnis:')
print('beste Route:', besteRoute)
print('beste Länge:', besteLaenge)
print()

#Erstellung des Graphens
plt.figure(1)
plt.plot(xAchse, listeBesteLaenge, label='Beste Laenge')
plt.plot(xAchse, listeAktuelleLaenge, label='Aktuelle Laenge')
plt.title('Statistischer Zufall')
plt.xlabel('Anzahl Episoden')
plt.ylabel('Laenge')
plt.legend()

# Save the plot as an image
plt.savefig('4.1.png')

# Show the plot
plt.show()


#exakte Lösung
'''
print('kürzeste Rundreise')
(minRoute, minLaenge) = minimaleRundreise(g, 'Bonn')
print('Route:', minRoute)
print('Länge:', minLaenge)
print()
'''
