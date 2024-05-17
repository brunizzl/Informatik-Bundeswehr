

def baue_spielfeld() -> list[list[int]]:
    return [
        [4, 1, 0,   0, 6, 5,   0, 0, 7],
        [0, 0, 6,   0, 0, 7,   4, 8, 0],
        [2, 0, 7,   4, 9, 0,   0, 0, 6],
        
        [0, 6, 0,   0, 7, 0,   1, 0, 0],
        [3, 0, 1,   5, 0, 0,   0, 7, 2],
        [0, 9, 0,   0, 4, 2,   3, 0, 8],
        
        [1, 0, 8,   6, 0, 0,   0, 2, 9],
        [0, 2, 0,   0, 1, 8,   6, 4, 0],
        [6, 0, 0,   3, 0, 0,   0, 1, 0]
        ]

def zeige_spielfeld(spielfeld: list[list[int]]):
    def print_linie():
        print("  +-------+-------+-------+")
        
    print("    1 2 3   4 5 6   7 8 9")
    for zeile_nr in range(9):
        if zeile_nr % 3 == 0:
            print_linie()
        print(zeile_nr + 1, end = " ")
        for spalte_nr in range(9):
            if spalte_nr % 3 == 0:
                print("|", end = " ")
            eintrag = spielfeld[zeile_nr][spalte_nr]
            if eintrag != 0:
                print(eintrag, end = " ")
            else:
                print(end = "  ")
        print("|")
    print_linie()
    
def gueltig(spielfeld: list[list[int]]) -> bool:
    # teste Zeilen
    for zeile in spielfeld:
        for zahl in range(1, 10):
            vorkommen = 0
            for eintrag in zeile:
                if eintrag == zahl:
                    vorkommen += 1
            if vorkommen > 1:
                return False
                
    #teste spalten
    for spalte_nr in range(9):
        for zahl in range(1, 10):
            vorkommen = 0
            for zeile_nr in range(9):
                eintrag = spielfeld[zeile_nr][spalte_nr]
                if eintrag == zahl:
                    vorkommen += 1
            if vorkommen > 1:
                return False
                
    #teste bloecke
    for block_zeile_nr in range(3):
        for block_spalte_nr in range(3):
            for zahl in range(1, 10):
                vorkommen = 0
                for zeile_delta in range(3):
                    for spalte_delta in range(3):
                        zeile_nr = 3 * block_zeile_nr + zeile_delta
                        spalte_nr = 3 * block_spalte_nr + spalte_delta
                        eintrag = spielfeld[zeile_nr][spalte_nr]
                        if eintrag == zahl:
                            vorkommen += 1
                if vorkommen > 1:
                    return False
    
    return True
    

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

def naechster_zug(spielfeld: list[list[int]]):
    while True:
        zeile_nr = int_eingabe("Zeile: ", 1, 9) - 1
        spalte_nr = int_eingabe("Spalte: ", 1, 9) - 1
        if spielfeld[zeile_nr][spalte_nr] != 0:
            print("Schon belegt :(")
        else:
            eintrag = int_eingabe("Wert: ", 1, 9)
            spielfeld[zeile_nr][spalte_nr] = eintrag
            if gueltig(spielfeld):
                return            
            print("Illegal :(")    
            spielfeld[zeile_nr][spalte_nr] = 0
            
def fertig(spielfeld: list[list[int]]) -> bool:
    for zeile in spielfeld:
        for eintrag in zeile:
            if eintrag == 0:
                return False
                
    return True
    
def spielen():
    feld = baue_spielfeld()
    while not fertig(feld):
        zeige_spielfeld(feld)
        naechster_zug(feld)
    
if __name__ == "__main__":
    spielen()
    