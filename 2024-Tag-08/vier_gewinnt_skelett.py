
# die oberste zeile hat index 0
def baue_spielfeld(breite: int, hoehe: int) -> list[list[str]]:
    # eine zeile ist eine liste von str der laenge "breite".
    # das gesamte spielfeld ist eine liste von zeilen der laenge "hoehe".
    pass

def zeige_spielfeld(feld: list[list[str]]):
    # gehe zeilenweise durch das feld und eintraegeweise durch jede zeile
    # tipp: print("Hallo", end = "") gibt Hallo auf der Konsole aus ohne Zeilenumbruch danach.
    # bonus: gebe als extrazeile die spaltennummern aus
    pass

def int_eingabe(msg: str, min: int, max: int) -> int:
    # frage den benutzer nach einer eingabe, bis er eine zahl >= min und <= max eingibt.
    # diese ist das ergebnis der funktion.
    pass    

def naechster_zug(feld: list[list[str]]) -> int:
    # frage den benutzer nach einer eingabe, bis er eine gueltige, noch nicht volle spalte angibt.
    # diese ist das ergebnis der funktion.
    pass
            
def gewonnen(feld: list[list[str]], spieler: str) -> bool: 
    #horizontal:
    for zeile in feld:
        streak = 0
        for wert in zeile:
            if wert == spieler:
                streak += 1
            else:
                streak = 0
                
            if streak == 4:
                return True
                
    #vertikal:
    for spalten_i in range(len(zeile)):
        streak = 0
        for zeilen_i in range(len(feld)):
            wert = feld[zeilen_i][spalten_i]
            if wert == spieler:
                streak += 1
            else:
                streak = 0
                
            if streak == 4:
                return True
    
    #diagonal von oben links nach unten rechts:
    for zeilen_start in range(len(feld) - (4 - 1)):
        for spalten_start in range(len(zeile) - (4 - 1)):
            streak = 0
            for i in range(4):
                wert = feld[zeilen_start + i][spalten_start + i]
                if wert == spieler:
                    streak += 1
                else:
                    streak = 0
                    
                if streak == 4:
                    return True

    #diagonal von oben rechts nach unten links:
    for zeilen_start in range(4 - 1, len(feld)):
        for spalten_start in range(len(zeile) - (4 - 1)):
            streak = 0
            for i in range(4):
                wert = feld[zeilen_start - i][spalten_start + i]
                if wert == spieler:
                    streak += 1
                else:
                    streak = 0
                    
                if streak == 4:
                    return True        
    
    return False
    

def spielen():
    breite = int_eingabe("Breite: ", 4, 10)
    hoehe = int_eingabe("Hoehe: ", 4, 20)
    feld = baue_spielfeld(breite, hoehe)
    while True:
        for spieler in ["X", "O"]:
            # hier bitte spiellogik einfuegen
            pass



  
    
    
    
    
    
    
    
    
    
    
        
