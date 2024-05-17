

def fun(i: int) -> None:
    if i > 0:
        i = i - 1
        fun(i)
    return
    
def fakultaet(n: int) -> int:
    ergebnis = 1 # diese Variable existiert nur, solange fakultaet berechnet wird.
    while n > 0:
        ergebnis *= n
        n -= 1
    return ergebnis # beende Funktion und gebe ergebnis zurueck

def fakultaet_2(n: int) -> int:
    if n == 0:
        return 1
    else:
        ergebnis = n * fakultaet_2(n - 1)
        return ergebnis

def fibonacci(n: int) -> int:
    a = 0 # zeroth fibonacci number
    b = 1 # first fibonacci number
    while n > 0:
        # advance both a and b to next
        new = a + b #<- neue Zeile
        a = b
        b = new #<- geaenderte Zeile
        # repeat n times
        n = n - 1
    # now a is the n-th fibonacci number
    return a


def fibonacci_2(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    vorletzte = fibonacci_2(n - 2)
    letzte = fibonacci_2(n - 1)
    diese = vorletzte + letzte
    return diese


















