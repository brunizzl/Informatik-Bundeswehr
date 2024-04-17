
#Aufgabe 1
def liste_test():
    #1.
    x = [1, 2, 5, 4, 3]
    
    #2.
    print(x[0])
    print(x[1])
    print(x[4])
    print(x[3])
    print(x[2])

    #3.
    x[2] = 3
    x[4] = 5
    print(x)

    #4.
    y = x[1:4]
    #y= [x[1], x[2], x[3]]
    print(y)

    #5.
    y[0] = -2

    #6.
    if x[1] == y[0]:
        print("x und y teilen speicher")
    else:
        print("x und y teilen keinen speicher")

    #7.
    z = x

    #8.
    z[1] = -20

    #9.
    print(x[1])
    

liste_test()

#Aufgabe 2
def liste_summe_alt(l: list[int]) -> int:
    summe = 0
    i = 0
    while i < len(l):
        #summe = summe + l[i]
        summe += l[i]
        
        #i = i + 1
        i += 1

    return summe

#Aufgabe 2
def liste_summe(l: list[int]) -> int:
    summe = 0
    for e in l:
        #summe = summe + e
        summe += e

    return summe

#Aufgabe 3
def tausche(l: list, i1: int, i2: int):
    #erinnere l[i1] bevor wir es ueberschreiben
    temp = l[i1]
    l[i1] = l[i2]
    l[i2] = temp

#Aufgabe 4
def liste_umdrehen(l: list):
    #laufe gleichzeitig von links (i1) und rechts (i2)
    i1 = 0
    i2 = len(l) - 1
    while i1 < i2:
        tausche(l, i1, i2)
        i1 += 1
        i2 -= 1

#Aufgabe 5
def sortiere(l: list[int]):
    #anmerkung: range(blub) ist identisch zu range(0, blub) 
    for _ in range(len(l)):
        i1 = 0
        i2 = 1
        while i2 < len(l):
            if l[i1] > l[i2]:
                tausche(l, i1, i2)
            i1 += 1
            i2 += 1









