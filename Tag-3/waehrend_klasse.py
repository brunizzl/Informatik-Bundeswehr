
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

def float_zu_str(x: float) -> str:
    ohne_vorzeichen = str(abs(x))
    if x < 0:
        vorzeichen = "- "
    else:
        vorzeichen = "+ "
    return vorzeichen + ohne_vorzeichen

def summe_von_bis(a: int, b: int) -> int:
    n = a
    summe = 0
    while n <= b:
        summe += n
        n += 1
    return summe

print(summe_von_bis((0 + 2 - 3) * -1, 100))
















