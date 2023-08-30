#Fibonaccizahlen
aktuelle = 0
naechste = 1

n = 0
while n < 20:
    print(aktuelle)
    #berechne uebernächste Fibonaccizahl
    uebernaechste = aktuelle + naechste
    
    #aktualisiere die Variablen (Reihenfolge wichtg)
    aktuelle = naechste
    naechste = uebernaechste
    n += 1

