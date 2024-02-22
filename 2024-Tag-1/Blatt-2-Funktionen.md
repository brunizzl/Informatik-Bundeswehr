
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


## Aufgabe 2
`h(h(h(-6)))`


## Aufgabe 3
`f(3 - g(4) * h(0))`


## Aufgabe 4
`1 + g(2 + 3 + 4) + 5 + h(6)`


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


## Aufgabe 6
`h(h(h(-6)))`


## Aufgabe 7
`f(3 - g(4) * h(0))`


## Aufgabe 8
`1 + g(2 + 3 + 4) + 5 + h(6)`


## Aufgabe 9
Die gegebenen Ausdrücke sind die Selben wie in Aufgaben 1, 2, 3 und 4.
Fällt ihnen ein Unterschied hinsichtlich der benötigten Rechenschitte auf?


# Weitere Regeln:
- Es können jetzt auch unbekannte Variablen auftreten (etwa `x`)
  Diese werden exakt gleich behandelt, als wären sie Ergebnis einer von uns aufgeschriebenen Rechnung.


## Aufgabe 10
`f(x - 2) + 3`


## Aufgabe 11
`h(h(h(x)))`


## Aufgabe 12
`f(x - y) * h(x)`


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


## Aufgabe 14
```
hhh(x):
    h(h(h(x)))
```


## Aufgabe 15
```
kernel(x, y):
    f(x - y) * h(x)
```




