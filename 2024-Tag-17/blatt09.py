import sortieren

liste = [1, 5, -2, 2, 1, 0, 100, -3, 2, 8, -12]

# beispiel, wie man die bibliothek "sortieren" nutzt
print("Test:", sortieren.mergesort(liste))



# Aufgabe 2
def groesser(x: int, y: int) -> bool:
    return x > y

print("Nr 2:", sortieren.mergesort_mit(groesser, liste))



# Aufgabe 3
def kleinerer_betrag(x: int, y: int) -> bool:
    return abs(x) < abs(y)

print("Nr 3:", sortieren.mergesort_mit(kleinerer_betrag, liste))



# Aufgabe 4
def naeher_an_5(x: int, y: int) -> bool:
    return kleinerer_betrag(x - 5, y - 5)

print("Nr 4:", sortieren.mergesort_mit(naeher_an_5, liste))



# Aufgabe 5
def kleinster_teiler(x: int) -> int:
    for y in range(2, x):
        if x % y == 0:
            return y
    return x



# Aufgabe 6
def kleinerer_teiler(x: int, y: int) -> bool:
    return kleinster_teiler(abs(x)) < kleinster_teiler(abs(y))
    
print("Nr 6:", sortieren.mergesort_mit(kleinerer_teiler, liste))



# Aufgabe 6 Bonus
def primfaktoren(x: int) -> list[int]:
    faktoren = []
    if x < 0:
        x *= -1;
        faktoren.append(-1)
    if x == 1:
        faktoren.append(1)
    while x > 1:
        faktor = kleinster_teiler(x)
        faktoren.append(faktor)
        x //= faktor
            
    return faktoren
    
def kleinere_primfaktoren(x: int, y: int) -> bool:
    # wenn man zwei listen in ihrer groesse vergleicht, is die liste kleiner, 
    # die an der ersten stelle, an der beide listen ungleich sind, 
    # den kleineren eintrag hat.
    # wenn die eine liste mit dem anfang der anderen liste identisch ist, 
    # aber kuerzer ist, dann ist die kuerzere liste kleiner.
    # (siehe "lexikographische ordnung")
    return primfaktoren(x) < primfaktoren(y)
 
print("Nr 6:", sortieren.mergesort_mit(kleinere_primfaktoren, liste), "(Bonus)")



# Aufgabe 7
def ist_primzahl(x: int) -> bool:
    return x > 1 and kleinster_teiler(x) == x

def primzahlen_zuerst(x: int, y: int) -> bool:
    x_ist_prim = ist_primzahl(abs(x))
    y_ist_prim = ist_primzahl(abs(y))
    if x_ist_prim != y_ist_prim:
        # vergleich von bool verhaelt sich, 
        # als ob True == 1 und False == 0
        return x_ist_prim > y_ist_prim
    return kleinerer_teiler(x, y)
    
print("Nr 7:", sortieren.mergesort_mit(primzahlen_zuerst, liste))



# Aufgabe 8:
coole_zahlen = [100, 2, 42, 240, 1337]
def ist_cool(x: int) -> bool:
    return (x in coole_zahlen)
    
def coole_zuerst(x: int, y: int) -> bool:
    x_ist_cool = ist_cool(x)
    y_ist_cool = ist_cool(y)
    if x_ist_cool != y_ist_cool:
        return x_ist_cool > y_ist_cool
    return x < y

print("Nr 8:", sortieren.mergesort_mit(coole_zuerst, liste))