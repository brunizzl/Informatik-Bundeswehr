

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

def zeige_spielfeld(spielfeld: list[list[int]], original: list[list[int]]):
    def print_linie():
        print("  +----------+----------+----------+")
        
    print("    1  2  3    4  5  6    7  8  9")
    for zeile_nr in range(9):
        if zeile_nr % 3 == 0:
            print_linie()
        print(zeile_nr + 1, end = " ")
        for spalte_nr in range(9):
            if spalte_nr % 3 == 0:
                print("|", end = " ")
                
            eintrag = spielfeld[zeile_nr][spalte_nr]
            if eintrag != 0:
                print(eintrag, end = "")
                if original[zeile_nr][spalte_nr] == 0:
                    print(end = "' ")
                else:
                    print(end = "  ")
            else:
                print(end = "   ")
        print("|")
    print_linie()
    
def gueltig_um(spielfeld: list[list[int]], zeile_nr: int, spalte_nr: int) -> bool:
    eintrag = spielfeld[zeile_nr][spalte_nr]
    if eintrag == 0:
        return True
    
    # teste zeile
    for i in range(9):
        if spielfeld[zeile_nr][i] == eintrag and i != spalte_nr:
            return False
    
    # teste spalte
    for i in range(9):
        if spielfeld[i][spalte_nr] == eintrag and i != zeile_nr:
            return False
                
    #teste block
    block_zeile_start = zeile_nr - (zeile_nr % 3)
    block_spalte_start = spalte_nr - (spalte_nr % 3)
    for zeile_delta in range(3):
        for spalte_delta in range(3):
            z = block_zeile_start + zeile_delta
            s = block_spalte_start + spalte_delta
            if spielfeld[z][s] == eintrag and (z != zeile_nr or s != spalte_nr):
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

def naechster_zug(spielfeld: list[list[int]], original: list[list[int]]):
    while True:
        zeile_nr = int_eingabe("Zeile: ", 1, 9) - 1
        spalte_nr = int_eingabe("Spalte: ", 1, 9) - 1
        if original[zeile_nr][spalte_nr] != 0:
            print("Der Wert ist nicht veränderbar :(")
        else:
            eintrag = int_eingabe("Wert: ", 0, 9) #<- unterschied: startet bei 0
            alter_eintrag = spielfeld[zeile_nr][spalte_nr]
            spielfeld[zeile_nr][spalte_nr] = eintrag
            if gueltig_um(spielfeld, zeile_nr, spalte_nr):
                return
            print("Illegal :(")    
            spielfeld[zeile_nr][spalte_nr] = alter_eintrag
            
def fertig(spielfeld: list[list[int]]) -> bool:
    for zeile in spielfeld:
        for eintrag in zeile:
            if eintrag == 0:
                return False
                
    return True
    
def spielen():
    feld = baue_spielfeld()
    original = baue_spielfeld()
    while not fertig(feld):
        zeige_spielfeld(feld, original)
        naechster_zug(feld, original)

if __name__ == "__main__":
    spielen()
    