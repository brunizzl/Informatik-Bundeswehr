def moin() -> str:
    x = "ja"
    y = "moin"
    return x + " " + y

def fibonacci(n: int) -> int:
    a = 0
    b = 1
    while n > 0:
        naechste = a + b
        a = b
        b = naechste
        n = n - 1

    return a

def test():
         
    a = moin()
    b = a + "!"
    
    c = fibonacci(5)
    d = fibonacci(fibonacci(3))
    
    e = d - c
    print(e)

# info: die funktion ist doch korrekt,
# 2024 = 2 hoch 11, also muessen 11 nullen 
# dahinter sein (stellen rechts davon sind 
# 2 hoch 10 bis inklusive 2 hoch 0 -> 11 stellen)
def zahl_als_str_10(n: int) -> str:
    z = 1
    while z * 2 <= n:
        z = z * 2
    
    erg = ""
    while z != 0:
        if n - z >= 0:
            erg = erg + "1"
            n = n - z
        else:
            erg = erg + "0"
        z = z // 2
        
    return erg

def laengerer(a: str, b: str) -> str:
    if len(a) < len(b):
        return b
    else:
        return a


def float_zu_str(x: float) -> str:
    if x < 0:
        vorz = "- "
    else:
        vorz = "+ "

    return vorz + str(abs(x))


























