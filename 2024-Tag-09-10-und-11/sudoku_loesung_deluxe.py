

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


# wenn spielfeld lösbar ist: schreibt die lösung ins spielfeld und gibt "True" zurück
# wenn nicht: lässt spielfeld wie vorher und gibt "False" zurück.
def loesung(spielfeld: list[list[int]]) -> bool:
    for zeile_nr in range(9):
        for spalte_nr in range(9):
            if spielfeld[zeile_nr][spalte_nr] == 0:
                for wert in range(1, 10):
                    spielfeld[zeile_nr][spalte_nr] = wert
                    if gueltig_um(spielfeld, zeile_nr, spalte_nr):
                        if loesung(spielfeld):
                            return True
                spielfeld[zeile_nr][spalte_nr] = 0
                return False
                
    # hier kommen wir hin, wenn das spielfeld bereits gelöst ist. 
    # das passiert bei der rekursiven variante IMMER (wenn es eine lösung gibt).
    return True


# wenn spielfeld lösbar ist: schreibt die lösung ins spielfeld und gibt "True" zurück
# wenn nicht: lässt spielfeld wie vorher und gibt "False" zurück.
def loesung_iter(spielfeld: list[list[int]]) -> bool:
    stack = []

    # wenn es noch eine leere position gibt: füge diese zu "stack" hinzu und gebe "True" zurück.
    # sonst: gebe "False" zurück
    def finde_neue_stelle() -> bool:
        for zeile_nr in range(9):
            for spalte_nr in range(9):
                if spielfeld[zeile_nr][spalte_nr] == 0:
                    stack.append((zeile_nr, spalte_nr))
                    return True
        return False

    # wenn der wert an der letzten position im stack noch nach oben abgeändert werden kann,
    # tue dies und gebe "True" zurück.
    # sonst: setzte diesen letzten eintrag wieder auf 0, lösche die position aus 
    # dem stack und gebe "False" zurück.
    def naechster_wert_alte_stelle() -> bool:
        (zeile_nr, spalte_nr) = stack[-1]
        while True:
            spielfeld[zeile_nr][spalte_nr] += 1
            if spielfeld[zeile_nr][spalte_nr] > 9:
                spielfeld[zeile_nr][spalte_nr] = 0
                stack.pop()
                return False
            if gueltig_um(spielfeld, zeile_nr, spalte_nr):
                return True
    
    # schreibe die erste freie position in "stack"
    if not finde_neue_stelle():
        # hier kommen wir hin, wenn das spielfeld bereits gelöst ist. 
        # das passiert bei der iterativen variante nur, wenn wir wirklich nur 
        # ein schon gelöstes feld lösen wollen.
        return True
        
    while True:
        if len(stack) == 0:
            # beim der ersten iteration der "while True" schleife können wir nicht hier landen,
            # weil wir die schleife nur betreten, wenn es eine leere position gab. (siehe hier drüber)
            return False
            
        # gerade wurde entweder eine neue position in "stack" eingetragen, 
        # oder die letzte position gelöscht, weil es keinen gültingen wert dafür gab.
        # so oder so haben wir jetzt wieder eine stelle, an der wir einen neuen wert eintragen müssen.
        if naechster_wert_alte_stelle():
            # wenn wir hier sind, ist uns gerade gelungen 
            # einen neuen wert in eine alte position zu schreiben.
            # also: probieren wir die nächste leere position zu finden.
            if not finde_neue_stelle():
                # wir haben keine leere position gefunden -> das sudoku ist gelöst!
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
        
        # extra teil um die automatischen lösungsfunktionen aufzurufen
        if zeile_nr == 0 and spalte_nr == 0:
            print("löse iterativ")
            loesung_iter(spielfeld)
            return
        if zeile_nr == 2 and spalte_nr == 2:
            print("löse rekursiv")
            loesung(spielfeld)
            return
            
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
        
    zeige_spielfeld(feld, original)


if __name__ == "__main__":
    spielen()

