
# gueltige werte sind "_", "X" und "O"
def baue_spielfeld() -> list[str]:
    return ["_"] * 9


def baue_metaspielfeld() -> list[list[str]]:
    #1. erzeuge eine neue variable "feld", initialisiert mit der leeren liste    
    #2. hänge an "feld" in einer schleife neun mal ein normales spielfeld dran    
    #3. gebe die fertige liste "feld" aus der funktion zurück
    
    pass # <- kann geloescht werden

def zeige_score(score: list[str]):
    print()
    print("Stand:   Indices:")
    print(score[0], score[1], score[2], "   1 2 3")
    print(score[3], score[4], score[5], "   4 5 6")
    print(score[6], score[7], score[8], "   7 8 9")

def zeige_metaspielfeld(meta: list[list[str]], score: list[str]):
    zeige_score(score)
    print()
    print("Gesamtes Spielfeld:")
    zeilen = [range(0, 3), range(3, 6), range(6, 9)]
    for meta_zeile in zeilen:
        for i, j, k in zeilen:
            for mi in meta_zeile:
                print(meta[mi][i], meta[mi][j], meta[mi][k], end = "    ")
            print()
        print()

def naechster_zug(feld: list[str], msg: str) -> int:
    while True:       
        zug = input(msg)
        # wenn "zug" nicht nur ziffern enthält (.isdigit()):
            # gebe fehlermeldung auf konsole aus
        # sonst:
            # erzeuge variable "i", als zug konvertiert zu int
            # ziehe von "i" 1 ab, damit indices 1 bis 9 zu 0 bis 8 werden.
            # wenn "i" kein gültiger index in "feld" ist:
                # gebe fehlermeldung auf konsole aus
            # sonst wenn "feld" an index "i" bereits belegt ist:
                # gebe fehlermeldung auf konsole aus
            # sonst:
                # "i" ist ergebnis und wird von dieser funktion zurückgegeben

def gewonnen(feld: list[str], spieler: str) -> bool:
    def alle_besetzt(a: int, b: int, c: int) -> bool:
        return (feld[a] == spieler 
            and feld[b] == spieler
            and feld[c] == spieler)
            
    #Zeilen
    return (alle_besetzt(0, 1, 2) 
        or alle_besetzt(3, 4, 5)
        or alle_besetzt(6, 7, 8)
        #Spalten
        or alle_besetzt(0, 3, 6)
        or alle_besetzt(1, 4, 7)
        or alle_besetzt(2, 5, 8)
        #Diagonalen
        or alle_besetzt(0, 4, 8)
        or alle_besetzt(6, 4, 2))

def spielen():
    score = baue_spielfeld()
    meta = baue_metaspielfeld()
    block = None
    while True:
        for spieler in ["X", "O"]:
            # zeige metaspielfeld auf konsole
            # erzeuge konsolenausgabe welcher spieler am zug ist
            
            # wenn "block" wert "None" hat oder index "block" in "score" nicht frei ist:
                # lasse spieler "block" wählen, der noch freier index in "score" ist.
            
            # erzeuge variable "i", die nächster zug von spieler ist. "i" muss ein freier index von 
            # dem (normalen) spielfeld in "meta" an index "block" sein.
            # setze den wert im (normalen) spielfeld in "meta" an index "block" mit index "i" auf "spieler"
            
            # wenn der spieler das normale feld an index "block" in "meta" gewonnen hat:
                # setze in "score" an index "block" auf "spieler"
                # wenn spieler das gesamte spiel gewonnen hat:
                    # gratuliere dem sieger auf der konsole
                    # beende die aktuelle funktion 
            # sonst wenn kein unterstrich mehr in "meta" an index "block" ist:
                # setze "score" an index "block" auf tilde
                # wenn es keine unterstriche mehr in "score" gibt:
                    # konsolenausgabe dass es unenschieden ist
                    # beende die aktuelle funktion 
            
            # setze "block" gleich "i"
            
            pass # <- kann geloescht werden
                



    


