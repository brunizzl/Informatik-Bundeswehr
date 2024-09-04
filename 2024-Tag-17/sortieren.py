
from collections.abc import Callable

# fuer einen beliebigen typen T, ist "liste" eine liste von variablen vom typ T
# und "kleiner" eine funktion, die sagt, ob das erste argument kleiner als das zweite argument ist.
# standartmaessig sollte also "kleiner(x, y)" das selbe ergebnis haben wie "x < y", 
# sprich entweder "True" oder "False".
def mergesort_mit[T](kleiner: Callable[[T, T], bool], liste: list[T]) -> list[T]:
    # Schritt 1
    if len(liste) <= 1:
        return liste
    
    # Schritt 2
    mitte = len(liste) // 2
    haelfte_1 = liste[:mitte]
    haelfte_2 = liste[mitte:]
    
    # Schritt 3
    sortiert_1 = mergesort_mit(kleiner, haelfte_1)
    sortiert_2 = mergesort_mit(kleiner, haelfte_2)
    
    # Schritt 4
    ergebnis = []
    
    # Schritt 5
    i1 = 0
    i2 = 0
    while i1 < len(sortiert_1) and i2 < len(sortiert_2):
        if kleiner(sortiert_1[i1], sortiert_2[i2]):
            ergebnis.append(sortiert_1[i1])
            i1 += 1
        else:
            ergebnis.append(sortiert_2[i2])
            i2 += 1
            
    ergebnis += sortiert_1[i1:]
    ergebnis += sortiert_2[i2:]
    
    # Schritt 6
    return ergebnis


def mergesort[T](liste: list[T]) -> list[T]:
    def kleiner(x: T, y: T) -> bool:
        return x < y
        
    return mergesort_mit(kleiner, liste)


def plus_kleiner_minus(x: int, y: int) -> bool:
    if x < 0 and y < 0:
        return x < y
    if x < 0:
        return False
    if y < 0:
        return True
    return x < y


if __name__ == "__main__":
    liste = [1, 5, -2, 2, 1, 0, 100, -3, 2, 8, -12]
    print("original liste:    ", liste)
    print("normales mergesort:", mergesort(liste))
    print("plus kleiner minus:", 
        mergesort_mit(plus_kleiner_minus, liste))


