
# Aufgabe 1
def tausche(liste: list, i1: int, i2: int):
    tmp = liste[i1]
    liste[i1] = liste[i2]
    liste[i2] = tmp

# Aufgabe 2
def tausche_test() -> list[int]:

    liste = [3, 0, -1, 3, 8, 2]
    tausche(liste, 0, 2)
    tausche(liste, -1, -2)
    tausche(liste, 2, -2)
    return liste

# Aufgabe 3
def bubblesort(liste: list[int]):
    for _ in range(len(liste)):
        for i in range(len(liste) - 1):
            i1 = i
            i2 = i + 1
            if liste[i1] > liste[i2]:
                tausche(liste, i1, i2)

# diese funktion produziert eine sortierte liste mit gleichen
# eintraegen wie das argument, zerstoert dabei allerdings das
# argument (am ende ist die variable "liste" leer).
# im gegensatz zu der bubblesortvariante aus aufgabe 3 wird hier
# nicht das jetzt-groesste an den richtigen ort gesetzt, sondern
# dass jetzt-kleinste.
def bubblesort_variante_marcel(liste: list[int]) -> list[int]:
    ergebnis = []
    for _ in range(len(liste)):
        kleinster = liste[0]
        i_kleinster = 0
        for i in range(1, len(liste)):
            if liste[i] < kleinster:
                kleinster = liste[i]
                i_kleinster = i
        # notwendig, damit wir nicht jeden durchlauf den selben
        # eintrag finden.
        liste.pop(i_kleinster)
        ergebnis.append(kleinster)
    return ergebnis

# Aufgabe 4
def insertionsort(liste: list[int]) -> list[int]:
    ergebnis = []
    for x in liste:
        i = len(ergebnis)
        while i > 0 and ergebnis[i - 1] > x:
            i -= 1
        ergebnis.insert(i, x)
        
    return ergebnis

# Aufgabe 5
def mergesort(liste: list[int]) -> list[int]:
    # Schritt 1
    if len(liste) <= 1:
        return liste
    
    # Schritt 2
    mitte = len(liste) // 2
    haelfte_1 = liste[:mitte]
    haelfte_2 = liste[mitte:]
    
    # Schritt 3
    sortiert_1 = mergesort(haelfte_1)
    sortiert_2 = mergesort(haelfte_2)
    
    # Schritt 4
    ergebnis = []
    
    # Schritt 5
    i1 = 0
    i2 = 0
    while i1 < len(sortiert_1) and i2 < len(sortiert_2):
        if sortiert_1[i1] <= sortiert_2[i2]:
            ergebnis.append(sortiert_1[i1])
            i1 += 1
        else:
            ergebnis.append(sortiert_2[i2])
            i2 += 1
            
    ergebnis += sortiert_1[i1:]
    ergebnis += sortiert_2[i2:]
    
    # Schritt 6
    return ergebnis
    
    
    
    


