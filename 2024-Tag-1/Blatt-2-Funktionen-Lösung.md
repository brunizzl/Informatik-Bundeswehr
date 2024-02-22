
# Regeln
- In jeder neuen Zeile darf nur eine der folgenen Operationen angewendet werden 
    - zwei Zahlen addieren (`+`)
    - zwei Zahlen subtrahieren (`-`)
    - zwei Zahlen multiplizieren (`*`)
    - zwei Zahlen dividieren (`/`)
    - eine Funktion anwenden (die Definition einsetzen)
- Zum Schluss muss der Ausdruck zu einer Zahl vereinfacht sein
- Zuerst werden Klammern, dann mal / geteilt, dann plus / minus ausgewertet
- eine Funktionsdefinition darf erst eingesetzt werden, wenn das Argument ausgewertet ist
- Wenn zwei Vereinfachungen vorgenommen werden könnten, hat die Linke Vorrang
- Vergessen Sie nicht beim Einsetzen einer Funktion entsprechend Klammern zu setzen!

Die in den Aufgaben vorkommenden Funktionen haben diese Abbildungsforschriften:
- `f(x) = 3 * x - 1`
- `g(x) = 2 * x * x`
- `h(x) = 1 - x / 3`


## Beispiel
`4 + g(3) * f(9 - 2)` <- Startausdruck

`4 + (2 * 3 * 3) * f(9 - 2)`

`4 + (6 * 3) * f(9 - 2)`

`4 + 18 * f(9 - 2)`

`4 + 18 * f(7)`

`4 + 18 * (3 * 7 - 1)`

`4 + 18 * (21 - 1)`

`4 + 18 * 20`

`4 + 360`

`364` <- Ergebnis


## Aufgabe 1
`f(1 - 2) + 3`

Lösung:
`f(1 - 2) + 3`

`f(-1) + 3`

`(3 * (-1) - 1) + 3`

`(-3 - 1) + 3`

`-4 + 3`

`-1`


## Aufgabe 2
`h(h(h(-6)))`

Lösung:
`h(h(h(-6)))`

`h(h(1 - (-6) / 3))`

`h(h(1 - (-2)))`

`h(h(3))`

`h(1 - 3 / 3)`

`h(1 - 1)`

`h(0)`

`1 - 0 / 3`

`1 - 0`

`1`



## Aufgabe 3
`f(3 - g(4) * h(0))`

Lösung:
`f(3 - g(4) * h(0))`

`f(3 - (2 * 4 * 4) * h(0))`

`f(3 - (8 * 4) * h(0))`

`f(3 - 32 * h(0))`

`f(3 - 32 * (1 - 0 / 3))`

`f(3 - 32 * (1 - 0))`

`f(3 - 32 * 1)`

`f(3 - 32)`

`f(-29)`

`3 * (-29) - 1`

`-87 - 1`

`-88`


## Aufgabe 4
`1 + g(2 + 3 + 4) + 5 + h(6)`

Lösung:
`1 + g(2 + 3 + 4) + 5 + h(6)`

`1 + g(5 + 4) + 5 + h(6)`

`1 + g(9) + 5 + h(6)`

`1 + (2 * 9 * 9) + 5 + h(6)`

`1 + (18 * 9) + 5 + h(6)`

`1 + 162 + 5 + h(6)`

`163 + 5 + h(6)`

`168 + h(6)`

`168 + (1 - 6 / 3)`

`168 + (1 - 2)`

`168 + (-1)`

`167`


# Weitere Regeln:
- Rechnungen dürfen ab jetzt nicht mehr tatsächlich ausgeführt werden, 
  dem Ergebnis wird stattdessen ein Name gegeben, 
  welcher an Stelle der Uhrsprünglichen Rechung eingesetzt wird.
- die "ausgeführte" Rechung kriegt eine eigene Zeile
- Es muss nicht jedes Mal alles neu aufgeschrieben werden wie im Beispiel, 
  man darf auch den Originalausdruck ändern.
- Achten Sie darauf, dass Namen die bereits von Funktionen benutzt 
  werden keine doppelte Bedeutung kriegen (`f`, `g` und `h`)


## Beispiel
```
4 + g(3) * f(9 - 2)
```

```
a = g(3)
4 + a * f(9 - 2)
```

```
a = g(3)
b = 9 - 2
4 + a * f(b)
```

```
a = g(3)
b = 9 - 2
c = f(b)
4 + a * c
```

```
a = g(3)
b = 9 - 2
c = f(b)
d = a * c
4 + d
```

```
a = g(3)
b = 9 - 2
c = f(b)
d = a * c
e = 4 + d
e
```

## Aufgabe 5
`f(1 - 2) + 3`

Lösung (kompakt aufgeschrieben):
```
a = 1 - 2
b = f(a)
c = b + 3
c
```


## Aufgabe 6
`h(h(h(-6)))`

Lösung (kompakt aufgeschrieben):
```
a = h(-6)
b = h(a)
c = h(b)
c
```



## Aufgabe 7
`f(3 - g(4) * h(0))`

Lösung (kompakt aufgeschrieben):
```
a = g(4)
b = h(0)
c = a * b
d = 3 - c
e = f(d)
e
```


## Aufgabe 8
`1 + g(2 + 3 + 4) + 5 + h(6)`

Lösung (kompakt aufgeschrieben):
```
a1 = 2 + 3
a2 = a1 + 4
a3 = g(a2)
a4 = 1 + a3
a5 = a4 + 5
a6 = h(6)
a7 = a5 + a6
a7
```


## Aufgabe 9
Die gegebenen Ausdrücke sind die Selben wie in Aufgaben 1, 2, 3 und 4.
Fällt ihnen ein Unterschied hinsichtlich der benötigten Rechenschitte auf?


# Weitere Regeln:
- Es können jetzt auch unbekannte Variablen auftreten (etwa `x`)
  Diese werden exakt gleich behandelt, als wären sie Ergebnis einer von uns aufgeschriebenen Rechnung.


## Aufgabe 10
`f(x - 2) + 3`

Lösung (kompakt aufgeschrieben):
```
a1 = x - 2
a2 = f(a1)
a3 = a2 + 3
a3
```


## Aufgabe 11
`h(h(h(x)))`

Lösung (kompakt aufgeschrieben):
```
a = h(x)
b = h(a)
c = h(b)
c
```


## Aufgabe 12
`f(x - y) * h(x)`

Lösung (kompakt aufgeschrieben):
```
a = x - y
b = f(a)
c = h(x)
d = b + c
```


# Eigene Funktionen
Die Regeln werden nicht inhaltlich erweitert, allerdings möchten wir jetzt 
eine Funktion selbst in das bekannte Format bringen. 


## Beispiel
```
bsp(x):
    4 + g(x) * f(x - 2)
```

```
bsp(x):
    a = g(x)
    4 + a * f(x - 2)
```

```
bsp(x):
    a = g(x)
    b = x - 2
    4 + a * f(b)
```

```
bsp(x):
    a = g(x)
    b = x - 2
    c = f(b)
    4 + a * c
```

```
bsp(x):
    a = g(x)
    b = x - 2
    c = f(b)
    d = a * c
    4 + d
```

```
bsp(x):
    a = g(x)
    b = x - 2
    c = f(b)
    d = a * c
    e = 4 + d
    e
```


## Aufgabe 13
```
fun(x):
    f(x - 2) + 3
```

Lösung (kompakt aufgeschrieben):
```
fun(x):
    a = x - 2
    b = f(a)
    c = b + 3
    c
```


## Aufgabe 14
```
hhh(x):
    h(h(h(x)))
```

Lösung (kompakt aufgeschrieben):
```
hhh(x):
    a = h(x)
    b = h(a)
    c = h(b)
    c
```


## Aufgabe 15
```
kernel(x, y):
    f(x - y) * h(x)
```

Lösung (kompakt aufgeschrieben):
```
kernel(x, y):
    a = x - y
    b = f(a)
    c = h(x)
    d = b * c
```




