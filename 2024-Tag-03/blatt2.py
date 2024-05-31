
#Aufgabe 5
def betrag(x: float) -> float:
    if x >= 0:
        return x
    else:
        return -x


#Aufgabe 6
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

n = 0
print("Test Aufgabe 6:")
while n < 10:
    print("fibonacci(", n, ") = ", fibonacci(n))
    n = n + 1
    
#Aufgabe 7
def int_zu_binaer(n: int) -> str:
    if n == 0:
        return "0"
    
    #es war nicht Teil der Aufgabenstellung negative Zahlen
    #zu beruecksichtigen.
    if n < 0:
        return "-" + int_zu_binaer(betrag(n))
        
    erg = ""
    while n != 0:
        erg = str(n % 2) + erg
        n = n // 2
        
    return erg
    
#Aufgabe 7 variante 2:
#(das Vorgehen haben wir nicht besprochen, entspricht aber eher der Rechnung,
#die ich im Kopf machen wuerde um nach Binaer zu konvertieren)
def int_zu_binaer_2(n: int) -> str:
    if n == 0:
        return "0"
        
    if n < 0:
        return "-" + int_zu_binaer_2(-n)

    #finde die groesste zweierpotenz die in n steckt
    _2_hoch = 1
    while _2_hoch <= n:
        _2_hoch = _2_hoch * 2
    _2_hoch = _2_hoch // 2
        
    #finde wiederholt die groesste zweierpotenz,
    #die <= (der rest von) n ist
    erg = ""
    while _2_hoch != 0:
        if n >= _2_hoch:
            #naechsstgroessere potenz gefunden -> ziehe sie ab
            n = n - _2_hoch
            erg = erg + "1"
        else:
            erg = erg + "0"
        
        _2_hoch = _2_hoch // 2
    
    return erg

print()
print("Test Aufgabe 7:")
print("64 in binär ist ", int_zu_binaer(64))
print("64 in binär ist ", int_zu_binaer_2(64))
print("50 in binär ist ", int_zu_binaer(50))
print("50 in binär ist ", int_zu_binaer_2(50))


#Aufgabe 8
def int_zu_dezimal(n: int) -> str:
    if n == 0:
        return "0"
    
    #es war nicht Teil der Aufgabenstellung negative Zahlen
    #zu beruecksichtigen.
    if n < 0:
        return "-" + int_zu_dezimal(betrag(n))
        
    erg = ""
    while n != 0:
        erg = str(n % 10) + erg
        n = n // 10
        
    return erg

print()
print("Test Aufgabe 8:")
print("64 in dezimal ist ", int_zu_dezimal(64))
print("50 in dezimal ist ", int_zu_dezimal(50))

#Aufgabe 9
def float_epsilon() -> float:
    eps = 1.0
    while 1.0 + eps != 1.0:
        eps = eps / 2
    
    return eps * 2

print()
print("Test Aufgabe 9:")
print("1 +   ε   == 1: ", 1 + float_epsilon() == 1)
print("1 + ε / 2 == 1: ", 1 + float_epsilon() / 2 == 1)

#Aufgabe 10
def euler() -> float:
    summe = 0.0
    summe_alt = -1.0 #wert egal, hauptsache nicht 0.0
    
    k = 0
    k_fakultaet = 1.0
    while summe_alt != summe:
        summe_alt = summe
        summe = summe + 1.0 / k_fakultaet
        k = k + 1
        k_fakultaet = k_fakultaet * k
    
    return summe

print()
print("Test Aufgabe 10:")
print("e = ", euler())






