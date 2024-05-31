def mal_3(x: int) -> int:
    return 3 * x

print("test:")
print(mal_3(2))
print(mal_3(3))



#Aufgabe 2
def fahrenheit_zu_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

#Aufgabe 3
def rankine_zu_fahrenheit(rankine: float) -> float:
    return rankine - 459.67


print("rankine_zu_fahrenheit(0) = ", rankine_zu_fahrenheit(0))

#Aufgabe 4
def rankine_zu_celsius(t: float) -> float:
    return fahrenheit_zu_celsius(rankine_zu_fahrenheit(t))

#Aufgabe 5
def sterne(n: int) -> str:
    return n * "*"

def sterne_im_dreieck(m: int):
    while m != 0:
        print(sterne(m))
        m = m - 1
    return

#Aufgabe 6
def betrag(x: int) -> int:
    if x < 0:
        return -x
    else:    
        return x

def max(x: int, y: int) -> int:
    if x > y:
        return x
    else:    
        return y

def zahlenquadrate(n: int):
    y = -n
    while y <= n:
        x = -n
        while x <= n:
            print(max(betrag(x), betrag(y)), end = " ")
            x = x + 1
            
        print()
        y = y + 1
        
#Aufgabe 7
def zahlenrauten(n: int):
    y = -n
    while y <= n:
        x = -n
        while x <= n:
            ziffer = betrag(x) + betrag(y)
            if ziffer <= n:
                print(ziffer, end = " ")
            else:
                print(" ", end = " ")
            x = x + 1
            
        print()
        y = y + 1
    
















    
