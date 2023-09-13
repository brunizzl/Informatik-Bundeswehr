
# f(x) = 1/2 * x^2 + 3
def f(x: float) -> float:
    return 1/2 * x ** 2 + 3
    
#n soll eine ganze zahl sein, dann ist auch das ergebnis eine ganze zahl
def fakultaet(n: int) -> int:    
    faku = 1
    while n > 0:
        faku *= n # fakultaet = fakultaet * n
        n -= 1 #n = n - 1
    return faku

def laengerer(a: str, b: str) -> str:
    if len(b) > len(a):
        return b
    else:
        return a

#Aufgabe 2
def float_zu_str(x: float) -> str:
    ohne_vorzeichen = str(abs(x))
    if x < 0:
        vorzeichen = " - "
    else:
        vorzeichen = " + "
    return vorzeichen + ohne_vorzeichen

def summe_von_bis(a: int, b: int) -> int:
    n = a
    summe = 0
    while n <= b:
        summe += n
        n += 1
    return summe
    
#Aufgabe 5
def poly_zu_str(poly: list[float]) -> str:
    ergebnis = str(poly[0])
    i = 1
    laenge = len(poly)
    while i < laenge:    
        koeff = poly[i]
        ergebnis += float_zu_str(koeff)
        ergebnis += " x^" + str(i)
        i += 1
    return ergebnis

#Aufgabe 6
def ableitung(poly: list[float]) -> list[float]:
    i = 1
    laenge = len(poly)
    ergebnis = (laenge - 1) * [0]
    while i < laenge:    
        koeff = poly[i]
        ergebnis[i - 1] = koeff * i
        i += 1
    return ergebnis

print(summe_von_bis((0 + 2 - 3) * -1, 100))
















