

#  baut:
#  +-----+-----+
#  | 1 4 |     |
#  | 3   | 1 4 |
#  +-----+-----+
#  | 2   |     |
#  |   3 |   1 |
#  +-----+-----+
def baue_spielfeld() -> list[list[int]]:
    return [
        [1, 4, 0, 0],
        [3, 0, 1, 4],
        [2, 0, 0, 0],
        [0, 3, 0, 1]
    ]

def print_eintrag(eintrag: int):
    if eintrag == 0:
        print(" ", end = " ")
    else:
        print(eintrag, end = " ")

def zeige_spielfeld(spielfeld: list[list[int]]):

    ## erste variante:
    #print(spielfeld[0])
    #print(spielfeld[1])
    #print(spielfeld[2])
    #print(spielfeld[3])

    ## zweite variante:
    #for zeile in spielfeld:
    #    print(zeile)

    ## dritte variante:
    #for z in range(4):
    #    print(spielfeld[z])

    ## bis hierhin ist die ausgabe immer identisch gewesen

    ## vierte variante:
    #for z in range(4):
    #    print(z + 1, " |", end = " ")
    #    print(spielfeld[z][0], end = " ")
    #    print(spielfeld[z][1], end = " ")
    #    print(spielfeld[z][2], end = " ")
    #    print(spielfeld[z][3], end = " ")
    #    print("|")

    ## fuenfte variante:
    #for z in range(4):
    #    print(z + 1, " |", end = " ")
    #    for s in range(4):
    #        print(spielfeld[z][s], end = " ")
    #    print("|")
    
    ## finale variante:
    print("     1 2   3 4")
    for z in range(4):
        if z == 0 or z == 2:
            print("   +-----+-----+")
        print(z + 1, " |", end = " ")
        for s in range(4):
            if s == 2:
                print("|", end = " ")
            print_eintrag(spielfeld[z][s])
        print("|")
    print("   +-----+-----+")


def gueltig_um(spielfeld: list[list[int]], zeile_nr: int, spalte_nr: int) -> bool:
    eintrag = spielfeld[zeile_nr][spalte_nr]
    
    # teste zeile
    for i in range(4):
        if spielfeld[zeile_nr][i] == eintrag and i != spalte_nr:
            return False
    
    # teste spalte
    for i in range(4):
        if spielfeld[i][spalte_nr] == eintrag and i != zeile_nr:
            return False
                
    #teste block
    block_zeile_start = zeile_nr - (zeile_nr % 2)
    block_spalte_start = spalte_nr - (spalte_nr % 2)
    for zeile_delta in range(2):
        for spalte_delta in range(2):
            z = block_zeile_start + zeile_delta
            s = block_spalte_start + spalte_delta
            if spielfeld[z][s] == eintrag and (z != zeile_nr or s != spalte_nr):
                return False
    
    return True


def loesung(spielfeld: list[list[int]], level: int) -> bool:
    print("level: ", level)
    #zeige_spielfeld(spielfeld)
    #input()
    for zeile_nr in range(4):
        for spalte_nr in range(4):
            if spielfeld[zeile_nr][spalte_nr] == 0:
                for eintrag in range(1, 5):
                    spielfeld[zeile_nr][spalte_nr] = eintrag
                    if gueltig_um(spielfeld, zeile_nr, spalte_nr):
                        if loesung(spielfeld, level + 1):
                            return True
                spielfeld[zeile_nr][spalte_nr] = 0
                return False

    return True
                
                
    
def spielen():
    feld = baue_spielfeld()
    zeige_spielfeld(feld)
    print(loesung(feld, 0))
    zeige_spielfeld(feld)
    















