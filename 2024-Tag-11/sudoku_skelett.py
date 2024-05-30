

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
    

def gueltig_um(spielfeld: list[list[int]], zeile_nr: int, spalte_nr: int) -> bool:
    pass # <- kann gelöscht werden
    
    # definiere eine variable "eintrag", die den aktuellen 
    #  wert des spielfeldes in zeile "zeile_nr" und spalte "spalte_nr" speichert
    
    # teste die zeile "zeile_nr":
    # für jede spalte soll geguckt werden, ob in zeile "zeile_nr" an dieser spalte ebendfalls der wert "eintrag" steht.
    # wenn ja, und diese spalte nicht "spalte_nr" ist, gebe "False" zurück.
    
    # teste die spalte "spalte_nr":
    # für jede zeile soll geguckt werden, ob in dieser zeile in spalte "spalte_nr" ebendfalls der wert "eintrag" steht.
    # wenn ja, und diese zeile nicht "zeile_nr" ist, gebe "False" zurück.
                
    # teste den block der position ("zeile_nr", "spalte_nr") enthält:
    # definiere eine variable "block_zeile_start", die den index der ersten zeile des blockes speichert
    # definiere eine variable "block_spalte_start", die den index der ersten spalte des blockes speichert
    # für alle zeilen von "block_zeile_start" bis vor ""block_zeile_start" + 3:
    #    für alle spalten von "block_spalte_start" bis vor ""block_spalte_start" + 3:
    #       teste, ob an dieser stelle ein zu "eintrag" identischer wert steht und die position von ("zeile_nr", "spalte_nr") unterschiedlich ist.
    #           wenn ja: gebe "False" zurück.
    
    # wenn alle tests durchgelaufen sind:
    # gebe "True" zurück.


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
    pass # <- kann gelöscht werden
    
    # in einer endlosschleife:
    #    definiere eine variable "zeile_nr", die vom benutzer zwischen 1 und (inklusive) 9 gewählt werden soll (tipp: nutze funktion "int_eingabe")
    #    ziehe 1 von "zeile_nr" ab und speichere das ergebnis wieder in "zeile_nr"
    #    definiere eine variable "spalte_nr", die vom benutzer zwischen 1 und (inklusive) 9 gewählt werden soll (tipp: nutze funktion "int_eingabe")
    #    ziehe 1 von "spalte_nr" ab und speichere das ergebnis wieder in "spalte_nr"
    #    wenn "spielfeld" an position ("zeile_nr", "spalte_nr") schon besetzt ist (also nicht eintrag 0 hat), gebe eine fehlermeldung aus.
    #    sonst:
    #        definiere eine variable "eintrag", die vom benutzer zwischen 1 und (inklusive) 9 gewählt werden soll (tipp: nutze funktion "int_eingabe")
    #        setzte "spielfeld" an position ("zeile_nr", "spalte_nr") auf den wert "eintrag"
    #        wenn "spielfeld" um position ("zeile_nr", "spalte_nr") gültig ist:
    #            return
    #        sonst:
    #            gebe eine fehlermeldung aus
    #            setzte "spielfeld" an position ("zeile_nr", "spalte_nr") wieder auf wert 0
    #            beginne die nächste iteration der endlosschleife
            
def fertig(spielfeld: list[list[int]]) -> bool:
    pass # <- kann gelöscht werden
    
    # wenn an irgend einer stelle in "spielfeld" der wert 0 steht, gebe "False" zurück.
    # sonst: gebe "True" zurück
    
def spielen():
    pass # <- kann gelöscht werden
    
    # definiere eine variable "feld", die das spielfeld speichert
    # solange das sudoku noch nicht fertig gelöst ist:
    #     zeige das aktuelle spielfeld auf der konsole an
    #     lasse den spieler den nächsten zug eingeben
    # wenn das spiel vorei ist: zeige noch ein letztes mal das spielfeld an
    
if __name__ == "__main__":
    spielen()
    