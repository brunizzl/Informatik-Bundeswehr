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




















    
