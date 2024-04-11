

#Aufgabe 5
def nikolaushaus_len(a: float) -> float:
    quadrat = a * 4
    fachwerk = 1.4142 * a * 2
    dach = 5 / 6 * a * 2
    return quadrat + fachwerk + dach
    
#Aufgabe 6
def patrone_len() -> float:
    return 2389 * nikolaushaus_len(2.0)

#Aufgabe 7
def patronen_fuer_linear_wachsend(n: int) -> float: 
    
    kosten = 0.0
    a = 2.0
    while n != 0:
        kosten = kosten + nikolaushaus_len(a)
        a = a + 2.0
        n = n - 1
        
    return kosten / patrone_len()

#Aufgabe 8
def patronen_fuer_exp_wachsend(n: int) -> float:
    
    kosten = 0.0
    a = 2.0
    while n != 0:
        kosten = kosten + nikolaushaus_len(a)
        a = a * 2.0
        n = n - 1
        
    return kosten / patrone_len()

#Aufgabe 9
print("  n | linear   | exp")
n = 1
while n <= 20:
    lin = patronen_fuer_linear_wachsend(n)
    exp = patronen_fuer_exp_wachsend(n)
    # diese form strings zu erzeugen ist neu,
    # hier erlaubt sie aber recht simpel eine
    # extrahuebsche tabelle.
    print(f"{n:>3} | {lin:5f} | {exp:5f}")
    n = n + 1






