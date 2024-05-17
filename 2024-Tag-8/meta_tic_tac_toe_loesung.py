
# gueltige werte sind "_", "X" und "O"
def baue_spielfeld() -> list[str]:
    return ["_"] * 9

def baue_metaspielfeld() -> list[list[str]]:
    feld = []
    for _ in range(9):
        feld.append(baue_spielfeld())
    
    return feld

def zeige_score(score: list[str]):
    print()
    print("Stand:   Indices:")
    print(score[0], score[1], score[2], "   1 2 3")
    print(score[3], score[4], score[5], "   4 5 6")
    print(score[6], score[7], score[8], "   7 8 9")

def zeige_metaspielfeld(meta: list[list[str]], score: list[str]):
    zeige_score(score)
    print()
    print("Gesamtes Spielfeld:")
    zeilen = [range(0, 3), range(3, 6), range(6, 9)]
    for meta_zeile in zeilen:
        for i, j, k in zeilen:
            for mi in meta_zeile:
                print(meta[mi][i], meta[mi][j], meta[mi][k], end = "    ")
            print()
        print()

def naechster_zug(feld: list[str], msg: str) -> int:
    while True:                
        zug = input(msg)
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
    score = baue_spielfeld()
    meta = baue_metaspielfeld()
    block = None
    while True:
        for spieler in ["X", "O"]:
            zeige_metaspielfeld(meta, score)
            print("Spieler", spieler, "ist am Zug.")
            
            if (block == None) or (score[block] != "_"):
                block = naechster_zug(score, "Wähle Block: ")           
            
            msg = "Zug in Block " + str(block + 1) + ": "
            i = naechster_zug(meta[block], msg)
            meta[block][i] = spieler
             
            if gewonnen(meta[block], spieler):
                score[block] = spieler
                if gewonnen(score, spieler):      
                    print("Spieler", spieler, "hat gewonnen!")
                    return    
            elif not "_" in meta[block]:
                score[block] = "~"
                if not "_" in score:
                    print("Unentschieden!")
                    return
            
            block = i

if __name__ == "__main__":
    spielen()



















    


