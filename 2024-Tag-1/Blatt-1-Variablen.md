
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


## Aufgabe 2
`(99 - 55 + 33 * 2) / 2 + 5 * 12`


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


## Aufgabe 4
```
(99 - 55 + 33 * 2) / 2 + 5 * 12
```


# Weitere Regeln:
- Es können jetzt auch unbekannte Variablen auftreten (etwa `x`)
  Diese werden exakt gleich behandelt, als wären sie Ergebnis einer von uns aufgeschriebenen Rechnung.


## Aufgabe 5
```
2 * blub + 36 * x * x * x - 14 * x * x + 333 * x - 13 * blub
```




