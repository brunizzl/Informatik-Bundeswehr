

#  baut:
#  +-----+-----+
#  |   1 | 4   |
#  | 2 3 |     |
#  +-----+-----+
#  | 4   | 3 2 |
#  |   2 | 1   |
#  +-----+-----+
def baue_spielfeld() -> list[list[int]]:
    return [
        [0, 1, 4, 0],
        [2, 3, 0, 0],
        [4, 0, 3, 2],
        [0, 2, 1, 0]
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
    
    
def spielen():
    feld = baue_spielfeld()
    zeige_spielfeld(feld)















