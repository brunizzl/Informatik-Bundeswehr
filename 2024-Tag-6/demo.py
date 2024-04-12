
def liste_max_alt(l: list[int]) -> int:
    bisher_max = l[0]
    i = 1
    while i < len(l):
        if bisher_max < l[i]:
            bisher_max = l[i]
        i = i + 1

    return bisher_max

def liste_max(l: list[int]) -> int:
    bisher_max = l[0]
    for e in l:
        if bisher_max < e:
            bisher_max = e

    return bisher_max

def zahl_als_bin_liste(n: int) -> list[int]:
    z = 1
    while z * 2 <= n:
        z = z * 2
    
    erg = []
    while z != 0:
        if n - z >= 0:
            erg = [1] + erg
            n = n - z
        else:
            erg = [0] + erg
        z = z // 2
        
    return erg

def plus_1(zahl: list[int]) -> list[int]:
    erg = zahl.copy()
    i = 0
    while i < len(zahl):
        if erg[i] == 0:
            erg[i] = 1
            return erg
        else:
            erg[i] = 0
        i += 1
    return erg + [1]

def range_liste(start: int, stop: int) -> list[int]:
    erg = [0] * (stop - start)
    i = 0
    while i < len(erg):
        erg[i] = start
        start += 1
        i += 1

    return erg

for x in range_liste(2, -10):
    print(x)
print("fertig!")










