
# speicher, damit "zufaellig" nicht immer selbe zahl berechnet
x = 1

# erzeugt eine pseudozufaellige zahl zwischen 0 und 2 hoch 64 minus 1
def zufaellig() -> int:
    
    # nutzt einen "linearen kongruenzgenerator"
    def lcg() -> int:
        global x
        # werte sind gewaehlt von donald knuth
        x = (x * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        # nutze nur mittlere bits fuer bessere qualitaet
        return (x >> 16) % (1 << 32)
        
    # wende generator doppelt an um laengere zahl zu erzeugen
    return lcg() * (1 << 32) + lcg()

# erzeugt eine pseudozufaellige zahl zwischen a und b minus 1
def zufaellig_von_bis(a: int, b: int) -> int:
    return (zufaellig() % (b - a)) + a

# erzeugt eine liste mit n pseudozufallszahlen zwischen 0 und 2 * n
def zufaellige_liste(n: int) -> list[int]:
    erg = [0] * n
    for i in range(n):
        erg[i] = zufaellig_von_bis(0, 2 * n)
    return erg
        