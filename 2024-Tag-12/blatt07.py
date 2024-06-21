
# f(x) = 5 * x + 3
def f(x: int) -> int:
    return 5 * x + 3


# Aufgabe 1
def quadrat_fun(x: int) -> int:
    
    ergebnis = x * x
    return ergebnis


# Aufgabe 2
def baue_quadrat_liste() -> list[int]:

    #y = []
    #for i in range(100):
    #    print(i)
    #    quadrat = quadrat_fun(i)
    #    y.append(quadrat)
    
    y = [0] * 100
    for i in range(100):
        y[i] = quadrat_fun(i)
        
    return y

quadrat_liste = baue_quadrat_liste()


# Aufgabe 3
def quadrat_taschenrechner():
    while True:
        text = input("Eingabe: ")
        if text.isdigit():
            x = int(text)
            if x < 0:
                print("Zahl zu klein :(")
            elif x > 99:
                print("Zahl zu groß :(")
            else:
                ## teil a):
                quadrat = quadrat_fun(x)
                ## teil b):
                #quadrat = quadrat_liste[x]
                print(quadrat)


# Aufgabe 4
def haeufiger_name_in_alter(alter: int) -> str:
    if alter < 10:
        return "Lina"
    elif alter < 20:
        return "Leon"
    elif alter < 30:
        return "Marvin"
    elif alter < 40:
        return "Janina"
    elif alter < 50:
        return "Tanja"
    elif alter < 60:
        return "Stefan"
    elif alter < 70:
        return "Angelika"
    elif alter < 80:
        return  "Ursula"
    elif alter < 90:
        return "Wolfgang"
    elif alter < 100:
        return "Ingeborg"
    else:
        return ""
    

# Aufgabe 5
haeufiger_name_in_lebensdekade = [
    "Lina",
    "Leon",
    "Marvin",
    "Janina",
    "Tanja",
    "Stefan",
    "Angelika",
    "Ursula",
    "Wolfgang",
    "Ingeborg",
]

# bonus für Aufgabe 6:
def haeufiger_name_in_alter_variante_2(alter: int) -> str:
    dekade = alter // 10
    if dekade < len(haeufiger_name_in_lebensdekade):
        return haeufiger_name_in_lebensdekade[dekade]
    else:
        return ""


# Aufgabe 7
def wurzel_abgerundet(x: int) -> int:
    for i in range(99):
        if quadrat_liste[i + 1] > x:
            return i
    
    return quadrat_liste[-1]

# bonus für Aufgabe 7:
def wurzel_bisektionsverfahren(x: float) -> float:
    untere_schranke = 0.0 # ist garantiert höchstens so groß wie wurzel von x
    obere_schranke = x # ist garantiert mindestens so groß wie wurzel von x
    
    # solange der relative unterschied zwischen den schranken zu groß ist, halbieren
    # wir unseren suchraum
    while (obere_schranke - untere_schranke) / (obere_schranke + 1e-10) > 1e-12:
        print("wurzel", x, "liegt zwischen", untere_schranke, "und", obere_schranke)
        mitte = (obere_schranke + untere_schranke) / 2.0
        if mitte ** 2 < x:
            untere_schranke = mitte
        else:
            obere_schranke = mitte

    return untere_schranke

# bonus 2 für Aufgabe 7:
def wurzel_newtonverfahren(x: float) -> float:
    # ist w die wurzel von x, löst w die gleichung w ** 2 == x,
    # oder äquivalent 0 == w ** 2 - x.
    # deswegen definieren wir f(w) = w ** 2 - x
    # und wollen die positive nullstelle von f finden.
    def f(w: float) -> float:
        return w ** 2 - x
    
    # erste ableitung von f
    def df(w: float) -> float:
        return 2 * w
        
    # eine tangente T von f an der stelle w_i hat die funktionsgleichung
    # T(w) = f(w_i) + (w - w_i) * df(w_i)
    # die aussage T(w) == 0 gilt damit für w == w_i - f(w_i) / df(w_i)
    # wenn f also eine gerade wäre, 
    # ist das w, für das T(w) == 0 ist, die wurzel von x.
    # wir tun jetzt so, als ob f wenigstens "lokal" "ähnlich aussieht" wie T
    # und finden so unsere wurzel.
    w_i = x
    for i in range(10): # gehe maximal 10 schritte
        print("für i =", i, "ist w_i =", w_i)
        # wenn f quasi null ist, ist w_i quasi die wurzel von x
        if abs(f(w_i)) < 1e-12:
            return w_i
        # sonst: tue so, als of f und T das selbe sind und
        # setze w_i zur nullstelle von T
        w_i = w_i - f(w_i) / df(w_i)
        
    return w_i



