## Aufgabe 1
- `*` ist ein Operator (der Malpunkt)
- `"Hallo"` ist ein Wert (vom Typ `str`)
- `-99.9` ist ein Wert (vom Typ `float`)
- `-` ist ein Operator (Minus)
- `/` ist ein Operator (Geteilt)
- `+` ist ein Operator (Plus)

## Aufgabe 2
`"Franz"` ist eine Zeichenkette (`str`), da Gänsefüßchen rechts und links davon gesetzt sind.

`franz` kann der Name einer Variablen sein, vorrausgesetzt es gab an einer bereits ausgeführten Stelle des Programms eine Zeile wie

        franz = 3

## Aufgabe 3
Zur Lösung kann jeder Ausdruck im Taschenrechnermodus in Python eingegeben werden. Will man den Typ direkt haben muss man `type(` Ausdruck `)` schreiben, e.g. `type(3 + 4)`.
- `0` ist vom Typ `int`
- `0.0` ist vom Typ `float`
- `"0"` ist vom Typ `str`
- `"0.0"` ist vom Typ `str`
- `3 + 4` wird zu `7` vom Typ `int` vereinfacht
- `3.0 + 4` wird zu `7.0` vom Typ `float` vereinfacht
- `"Hans" + " und " + "Franz"` wird zu `"Hans und Franz"` vom Typ `str` berechnet
- `20 % 7` wird zu `6` vom Typ `int` vereinfacht
- `20 / 7` wird zu `2.857142857142857` vom Typ `float` vereinfacht
- `3 > 4.0 + 4` wird zu `False` vom Typ `bool` vereinfacht

## Aufgabe 4
`"Ich aß gestern " + 78 + " Brötchen."` probiert `str` und `int` zu addieren. Wenn das Ziel die Zeichenkette `"Ich aß gestern 78 Brötchen."` sein soll, kann man etwa `"Ich aß gestern " + str(78) + " Brötchen."` schreiben.

`3 - "2"` hat das selbe Problem (mixen von `int` und `str`). Lösung: `3 - int("2")`





