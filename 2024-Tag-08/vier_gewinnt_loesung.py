
# die oberste zeile hat index 0
def baue_spielfeld(breite: int, hoehe: int) -> list[list[str]]:
    zeile = ["_"] * breite
    feld = []
    for _ in range(hoehe):
        feld.append(zeile.copy())
    return feld

def zeige_spielfeld(feld: list[list[str]]):
    print()
    for zeile in feld:
        for wert in zeile:
            print(wert, end = " ")
        print()
        
    for i in range(len(zeile)):
        print(i + 1, end = " ")
    print()

def int_eingabe(msg: str, min: int, max: int) -> int:
    while True:
        s = input(msg)
        if s.isdigit():
            i = int(s)
            if i < min:
                print("Zu klein.")
            elif i > max:
                print("Zu groß.")
            else:
                return int(s)
        else:
            print("Muss ne Zahl sein :(")
    

def naechster_zug(feld: list[list[str]]) -> int:
    breite = len(feld[0])
    while True:
        i = int_eingabe("Zug: ", 1, breite) - 1
        if feld[0][i] != "_":
            print("Schon besetzt.")
        else:
            return i
            
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
            zeige_spielfeld(feld)
            print("Spieler", spieler, "ist am Zug.")
            spalten_i = naechster_zug(feld)
            zeilen_i = hoehe - 1
            while feld[zeilen_i][spalten_i] != "_":
                zeilen_i -= 1
            feld[zeilen_i][spalten_i] = spieler
                
            if gewonnen(feld, spieler):
                print("Spieler", spieler, "hat gewonnen!")
                return
            if not "_" in feld[0]:
                print("Unentschieden!")
                return



  
    
    
    
    
    
    
    
    
    
    
        
