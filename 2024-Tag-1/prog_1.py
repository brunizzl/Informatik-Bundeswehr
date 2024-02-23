
def f(x: int) -> int:
    a = 3 * x
    b = a - 1
    return b

def h(x: int) -> float:
    return 1 - x / 3

def g(x: int) -> int:
    return 2 * x * x

def bsp(x: int) -> float:
    return 4 + g(x) * f(x - 2)

def heavy(x: float) -> float:
    if x >= 0:
        return 1
    return 0
    
def fakultaet(n: int) -> int:
    if n < 0:
        return -1
    
    ergebnis = 1
    while n > 0:
        ergebnis = (ergebnis * n)
        n = (n - 1)
        
    return ergebnis


print(fakultaet(100))
