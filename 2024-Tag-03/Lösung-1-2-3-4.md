## Aufgabe 1
$011111101000_{bin}$

$= 0 \cdot 2^{11} + 1 \cdot 2^{10} + 1 \cdot 2^9 + 1 \cdot 2^8 + 1 \cdot 2^7 + 1 \cdot 2^6 + 1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0$

$= 2^{10} + 2^9 + 2^8 + 2^7 + 2^6 + 2^5 + 2^3$

$= 1024 + 512 + 256 + 128 + 64 + 32 + 8$

$= 2024$

## Aufgabe 2
$1365_{dec}$

$=1364 + 1$

$= 2 \cdot 682 + 1$

$= 2 \cdot (682 + 0) + 1$

$= 2 \cdot (2 \cdot 341 + 0) + 1$

$= 2 \cdot (2 \cdot (340 + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot 170 + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (170 + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot 85 + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (84 + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 42 + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (42 + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 21 + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (20 + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 10 + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (10 + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 5 + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (4 + 1) + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 2 + 1) + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 1 + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1) + 0) + 1$

Nach etwas Ausfaktorisieren erhält man
$$1365_{dec} = 2^{10} + 2^8 + 2^6 + 2^4 + 2^2 + 2^0$$

Das Ausfaktorisieren ist aber eigentlich nicht notwendig, das Bitmuster kann man schon direkt von den einsen und nullen ablesen:
$$1365_{dec} = 10101010101_{bin}$$

Alternativ weitergerechnet nach dem Ausfaktorisieren:
$$1365_{dec} = 10000000000_{bin} + 100000000_{bin} + 1000000_{bin} + 10000_{bin} + 100_{bin} + 1_{bin} = 10101010101_{bin}$$

## Aufgabe 3
```
    0 1 0 1 0 1 0 0 1 1 0
+   0 1 0 1 0 0 1 0 0 1 1
  0 1 0 1 0 0 0 0 1 1 0
-------------------------
  0 1 0 1 0 0 1 1 1 0 0 1
```

## Aufgabe 4

### Zahl 1
$`011111101000_{bin} = 0111~1110~1000_{bin}`$

$0111_{bin} = 7_{hex}$

$1110_{bin} = 14_{dec} = E_{hex}$

$1000_{bin} = 8_{hex}$

$\implies 011111101000_{bin} = 7E8_{hex}$

### Zahl 2
$`10101010101_{bin} = 0101~0101~0101_{bin}`$

$0101_{bin} = 5_{hex}$

$\implies 10101010101_{bin} = 555_{hex}$

### Zahl 3
$`10100111001_{bin} = 0101~0011~1001_{bin}`$

$0101_{bin} = 5_{hex}$

$0011_{bin} = 3_{hex}$

$1001_{bin} = 9_{hex}$

$\implies 10100111001_{bin} = 539_{hex}$
