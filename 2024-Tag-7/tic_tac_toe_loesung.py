
# gueltige werte sind "_", "X" und "O"
def baue_spielfeld() -> list[str]:
    return ["_"] * 9
    

def zeige_spielfeld(feld: list[str]):
    print()
    print("Feld:   Züge:")
    print(feld[0], feld[1], feld[2], "  1 2 3")
    print(feld[3], feld[4], feld[5], "  4 5 6")
    print(feld[6], feld[7], feld[8], "  7 8 9")

def naechster_zug(feld: list[str]) -> int:
    while True:                
        zug = input("Zug: ")
        if not zug.isdigit():
            print("Gültig sind Züge von 1 bis 9.")
        else:
            i = int(zug) - 1
            if not i in range(0, 9):
                print("Gültig sind Züge von 1 bis 9.")
            elif feld[i] != "_":
                print("Feld schon besetzt.")
            else:
                return i

#Alternative Implementierung in tic_tac_toe_live.py
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
    feld = baue_spielfeld()
    while True:
        for spieler in ["X", "O", "S"]:
            zeige_spielfeld(feld)
            print("Spieler", spieler, "ist am Zug.")
            i = naechster_zug(feld)
            feld[i] = spieler
                
            if gewonnen(feld, spieler):
                print("Spieler", spieler, "hat gewonnen!")
                return
            if not "_" in feld:
                print("Unentschieden!")
                return



    


