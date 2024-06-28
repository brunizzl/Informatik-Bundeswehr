
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
# vorsicht: funktioniert noch nicht :0
def bubblesort(liste: list[int]):
    for i in range(len(liste) - 1):
        i1 = i
        i2 = i + 1
        if liste[i1] > liste[i2]:
            tausche(liste, i1, i2)

