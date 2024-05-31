
# Regeln
- In jeder neuen Zeile darf nur eine Rechnung ausgeführt werden
    - zwei Zahlen addieren (`+`)
    - zwei Zahlen subtrahieren (`-`)
    - zwei Zahlen multiplizieren (`*`)
    - zwei Zahlen dividieren (`/`)
- Zum Schluss muss der Ausdruck zu einer Zahl vereinfacht sein
- Zuerst werden Klammern, dann mal / geteilt, dann plus / minus ausgewertet
- Wenn zwei Vereinfachungen vorgenommen werden könnten, hat die Linke Vorrang


## Beispiel:
`4 + 3 * (9 - 2)` <- Startausdruck

`4 + 3 * 7`

`4 + 21`

`25` <- Ergebnis


## Aufgabe 1
`1 + 2 * (3 + 100 / (40 - 6 * 5) + 2) + (7 * 12) / 6 - 14`

Lösung:

`1 + 2 * (3 + 100 / (40 - 6 * 5) + 2) + (7 * 12) / 6 - 14`

`1 + 2 * (3 + 100 / (40 - 30) + 2) + (7 * 12) / 6 - 14`

`1 + 2 * (3 + 100 / 10 + 2) + (7 * 12) / 6 - 14`

`1 + 2 * (3 + 10 + 2) + (7 * 12) / 6 - 14`

`1 + 2 * (13 + 2) + (7 * 12) / 6 - 14`

`1 + 2 * 15 + (7 * 12) / 6 - 14`

`1 + 30 + (7 * 12) / 6 - 14`

`31 + (7 * 12) / 6 - 14`

`31 + 84 / 6 - 14`

`31 + 14 - 14`

`45 - 14`

`31`


## Aufgabe 2
`(99 - 55 + 33 * 2) / 2 + 5 * 12`

Lösung:

`(99 - 55 + 33 * 2) / 2 + 5 * 12`

`(44 + 33 * 2) / 2 + 5 * 12`

`(44 + 66) / 2 + 5 * 12`

`110 / 2 + 5 * 12`

`55 + 5 * 12`

`55 + 60`

`115`


# Weitere Regeln:
- Rechnungen dürfen ab jetzt nicht mehr tatsächlich ausgeführt werden, 
  dem Ergebnis wird stattdessen ein Name gegeben, 
  welcher an Stelle der ursprünglichen Rechung eingesetzt wird.
- die "ausgeführte" Rechung kriegt eine eigene Zeile
- Es muss nicht jedes Mal alles neu aufgeschrieben werden wie im Beispiel, 
  man darf auch den Originalausdruck ändern.


## Beispiel:
```
4 + 3 * (9 - 2)
```

```
a = 9 - 2
4 + 3 * a
```

```
a = 9 - 2
b = 3 * a
4 + b
```

```
a = 9 - 2
b = 3 * a
c = 4 + b
c
```


## Aufgabe 3
```
1 + 2 * (3 + 100 / (40 - 6 * 5) + 2) + (7 * 12) / 6 - 14
```

Lösung (ohne Rechenweg):
```
a = 6 * 5
b = 40 - a
c = 100 / b
d = 3 + c
e = d + 2
f = 2 * e
g = 1 + f
h = 7 * 12
i = h / 6
j = g + i
k = j - 14
k
```


## Aufgabe 4
```
(99 - 55 + 33 * 2) / 2 + 5 * 12
```

Lösung (ohne Rechenweg):
```
a = 99 - 55
b = 33 * 2
c = a + b
d = c / 2
e = 5 * 12
f = d + e
f
```


# Weitere Regeln:
- Es können jetzt auch unbekannte Variablen auftreten (etwa `x`).
  Diese werden exakt gleich behandelt, als wären sie Ergebnis einer von uns aufgeschriebenen Rechnung.


## Aufgabe 5
```
2 * blub + 36 * x * x * x - 14 * x * x + 333 * x - 13 * blub
```

Lösung (ohne Rechenweg):
```
a = 2 * blub
b = 36 * x
c = b * x
d = c * x
e = a + d
f = 14 * x
g = f * x
h = e - g
i = 333 * x
j = h + i
k = 13 * blub
l = j - k
l
```






