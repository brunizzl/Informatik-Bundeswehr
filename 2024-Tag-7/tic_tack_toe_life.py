
def baue_spielfeld() -> list[str]:

    #return ["_"] * 9

    spielfeld = []
    for i in range(9):
        spielfeld.append("_")

    return spielfeld

def zeige_spielfeld(feld: list[str]):
    #print(feld[0:3])
    #print(feld[3:6])
    #print(feld[6:9])
    print(feld[0], feld[1], feld[2], "    1 2 3")
    print(feld[3], feld[4], feld[5], "    4 5 6")
    print(feld[6], feld[7], feld[8], "    7 8 9")

def naechster_zug(feld: list[str]) -> int:
    while True:
        zeige_spielfeld(feld)
        s = input("Zug: ")
        if s.isdigit():
            i = int(s) - 1
            if i < 0:
                print("Zu Klein :(")
            elif i > 8:
                print("Zu Groß :(")
            elif feld[i] != "_":
                print("Schon voll :(")
            else:            
                return i
        else:
            print("Nur Ziffern bitte :(")
        
#Alternative Implementierung in tic_tac_toe_loesung.py
def gewonnen(feld: list[str], spieler: str) -> bool:
    #Zeilen
    if feld[0] == spieler and feld[1] == spieler and feld[2] == spieler:
        return True
    if feld[3] == spieler and feld[4] == spieler and feld[5] == spieler:
        return True
    if feld[6] == spieler and feld[7] == spieler and feld[8] == spieler:
        return True
    #Spalten
    if feld[0] == spieler and feld[3] == spieler and feld[6] == spieler:
        return True
    if feld[1] == spieler and feld[4] == spieler and feld[7] == spieler:
        return True
    if feld[2] == spieler and feld[5] == spieler and feld[8] == spieler:
        return True
    #Diagonalen
    if feld[0] == spieler and feld[4] == spieler and feld[8] == spieler:
        return True
    if feld[6] == spieler and feld[4] == spieler and feld[2] == spieler:
        return True
    
    return False

def spielen():
    feld = baue_spielfeld()
    while True:
        for spieler in ["X", "O"]:
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












