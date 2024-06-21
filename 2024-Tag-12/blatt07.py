
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

# bonus für Aufgabe 4:
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

