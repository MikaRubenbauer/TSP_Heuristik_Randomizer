from graph import *
from random import randint

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
    summeAbstaende = 0  # Variable für die Summe der Abstände initialisieren
    print('Initialisierung Route:', route)
    
    for knoten in g.getAlleKnoten():
        if knoten != startKnoten:
            knotenRestListe.append(knoten)  # Verwende `append` für Listenoperationen
    print('Initialisierung knotenRestListe:', knotenRestListe, '\n')
    
    while knotenRestListe:
        aktuellerKnoten = route[-1]  # Verwende `-1`, um das letzte Element der Liste zu erhalten
        print('Runde', zaehler)
        print('aktueller Knoten:', aktuellerKnoten)
        
        abstaende = [g.getGewichtKante(aktuellerKnoten, knoten) for knoten in knotenRestListe]
        for knoten, abstandKnoten in zip(knotenRestListe, abstaende):
            print('Knoten', knoten, 'hat Abstand:', abstandKnoten)
            summeAbstaende += abstandKnoten  # Addiere den Abstand zur Summe hinzu
        
        zufaelligeStelle = randint(0, len(knotenRestListe) - 1)
        ausgewaehlterKnoten = knotenRestListe.pop(zufaelligeStelle)  # Entferne den ausgewählten Knoten aus der Restliste
        route.append(ausgewaehlterKnoten)
        print('zufällig ausgewählter Knoten:', ausgewaehlterKnoten)
        
        zaehler += 1
        print('aktuelle Route', route)
        print('aktuelle Restliste', knotenRestListe)
        print()
        
    route.append(startKnoten)
    laengeRoute = laenge(g, route)
    
    durchschnittAbstaende = summeAbstaende / (len(route) - 1)  # Durchschnitt berechnen
    print("Durchschnittsabstand:", durchschnittAbstaende)  # Durchschnitt ausgeben
    
    return (route, laengeRoute)






# Erzeugung des Graph-Objekts
g = GraphMitDaten()
# Erzeugung der Knoten und Kanten aus einer GraphML-Datei
datei = open("graph_eu_6.xml", "r")
xml_quelltext = datei.read()
g.graphmlToGraph(xml_quelltext)

# Test der Rundreise-Algorithmus

# Näherungsverfahren 1
print('Näherungslösung Zufall')
for i in range(1,1000000):
    (minRoute, minLaenge) = rundreiseNaeherung(g, 'Bonn')
print('Ergebnis:')
print('Route:', minRoute)
print('Länge:', minLaenge)
print()

# exakte Lösung
print('kürzeste Rundreise')
(minRoute, minLaenge) = minimaleRundreise(g, 'Bonn')
print('Route:', minRoute)
print('Länge:', minLaenge)
print('\n\n\n')

print('13 Städte:')
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
print('kürzeste Rundreise')
(minRoute, minLaenge) = minimaleRundreise(g, 'Bonn')
print('Route:', minRoute)
print('Länge:', minLaenge)
print()



