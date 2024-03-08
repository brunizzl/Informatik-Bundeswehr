
## Das Dezimalsystem

Das Dezimalsystem ist unser normales Zahlensystem. Hier gibt es die Ziffern $0, 1, 2, \dots, 8, 9$. Das sind zehn verschiedene, deswegen auch der Name Zehnersystem. Um die Basis eindeutig zu machen, schreiben wir \\(\cdot _{dec})\\ als Index an eine Zahl, wenn sie im Dezimalsystem steht. Etwa schreiben wir einhundertsiebenundfünfzig als \\(157_{dec})\\.

Die Folge der drei Ziffern $1$, $5$ und $7$ wird als Zahl wiefolgt interpretiert:
$$157_{dec} = 1 \cdot 10^2 + 5 \cdot 10^1 + 7 \cdot 10^0$$
Die Position der einzelnen Ziffer ist dabei ausschlaggebend, mit welcher Zehnerpotenz sie multipliziert wird. Die letzte Stelle mit $10^0$, die vorletzte mit $10^1$, die vor-vorletzte mit $10^2$ und so weiter.
Allgemein, wenn eine Zahl im Dezimalsystem die $n + 1$ Ziffern $d_n, d_{n-1}, \dots, d_2, d_1, d_0$ hat, wird ihr Wert berechnet als
$$10^n \cdot d_n + 10^{n - 1} \cdot d_{n - 1} + \dots + 10^2 \cdot d_2 + 10^1 \cdot d_1 + 10^0 \cdot d_0$$
oder äquivalent
$$\sum_{k = 0}^n 10^k \cdot d_k$$

## Das Binärsystem

Der Computer kennt auf der untersten Ebene nur zwei Ziffern: $0$ und $1$. Entweder liegt auf einem Draht Spannung an, dann wird die Ziffer als $1$ gelesen oder es liegt keine Spannung an, dann wird die Ziffer als $0$ gelesen. 
In diesem System geschriebene Zahlen nennen wir Binärzahlen. Zur Erkennung schreiben wir als Index hinter eine Binärzahl $_{bin}$.
Zum Beispiel ist $101010_{bin}$ eine Binärzahl, $101010_{dec}$ dagegen ist eine Dezimalzahl die zufällig nur die Ziffern $0$ und $1$ enthält.

Die Zahlenwert von $101010_{bin}$ ist 
$$
101010_{bin} =
1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0
$$

Allgemein hat eine Zahl mit den $n + 1$ Binärziffern $b_{n}, b_{n - 1}, \dots, b_{2}, b_1, b_0$ also den Wert
$$2^n \cdot b_n + 2^{n - 1} \cdot b_{n - 1} + \dots + 2^2 \cdot b_2 + 2^1 \cdot b_1 + 2^0 \cdot b_0$$
oder äquivalent
$$
\sum_{k = 0}^n 2^k \cdot b_k
$$

Eindeutig sind damit $101010_{bin}$ und $101010_{dec}$ verschieden groß. Um eine Binärzahl für uns selber ins Dezimalsystem zu bringen müssen wir nur von Hand die entsprechende Rechnung durchführen. Im Beispiel also
$$101010_{bin}
= 1 \cdot 2^5 + + 1 \cdot 2^3 + 1 \cdot 2^1 
= 32 + 8 + 2
= 42_{dec}$$

Das ist deutlich kleiner als $101010_{dec}$.
Dem Computer würde diese Rechnung nicht helfen. Dort wird $32_{dec}$ als $100000_{bin}$ gespeichert. 
Der Ausdruck $(32 + 8 + 2)_{dec}$ also als $(100000 + 1000 + 10)_{bin}$. Wir laufen im Kreis, denn die Summe ist natürlich wieder $101010_{bin}$.

## Basisumrechnung

Beginnen wir damit eine Dezimalzahl in Binär zu schreiben. 
Wir müssen eigentlich nicht mehr tun als wiederholt (gegebenenfalls) minus 1 und geteilt durch 2 zu rechnen.

$55_{dec} = 54 + 1$

$= 2 \cdot 27 + 1$

$= 2 \cdot (26 + 1) + 1$

$= 2 \cdot (2 \cdot 13 + 1) + 1$

$= 2 \cdot (2 \cdot (12 + 1) + 1) + 1$

$= 2 \cdot (2 \cdot (2 \cdot 6 + 1) + 1) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (6 + 0) + 1) + 1) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot 3 + 0) + 1) + 1) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 + 1) + 0) + 1) + 1) + 1$

$= 2 \cdot (2 \cdot (2 \cdot (2 \cdot (2 \cdot 1 + 1) + 0) + 1) + 1) + 1$

Mit ein bisschen Umgruppieren erhalten wir
$$
55_{dec} = 2^5 \cdot 1 + 2^4 \cdot 1 + 2^3 \cdot 0 + 2^2 \cdot 1 + 2^1 \cdot 1 + 2^0 \cdot 1 = 110111_{bin}
$$

Die Rückrichtung ist konzeptionell nicht anders, nur für uns etwas mühsamer. Während durch zwei teilen für uns im Zehnersystem einfach war, ist durch 10 teilen im Binärsystem etwas anstrengender. 
Bevor wir darüber sprechen wie man im Binärsystem rechnet, ist es am einfachsten nur die Vorgehensweise aufzuschreiben und die tatsächliche Rechnung dem Computer anzuvertrauen.

1. Wir beginnen mit einer Zahl `n` im Binärsystem.
2. Die nächstwichtige Stelle im Dezimalsystem (beginnend mit der unwichtigsten) hat die Ziffer `n % 10`, wobei `%` "Teile und nehme den Rest" bedeutet.
3. Überschreibe `n` mit `n // 10`, wobei `//` "Teile und runde ab" bedeutet.
4. Wenn `n` nicht `0` ist springe zurück zu Schritt 2.

Die Binärziffern einer Zahl zu berechnen funktioniert auf dem selben Weg:
1. Wir beginnen mit einer Zahl `n`.
2. Die nächstwichtige Stelle im Binärsystem (beginnend mit der unwichtigsten) hat die Ziffer `n % 2`, wobei `%` "Teile und nehme den Rest" bedeutet.
3. Überschreibe `n` mit `n // 2`, wobei `//` "Teile und runde ab" bedeutet.
4. Wenn `n` nicht `0` ist springe zurück zu Schritt 2.

## Addition

Schriftlich addieren im Zehnersystem kennen wir aus dem Schulunterricht. Als Beispiel gehen wir die Rechnung $832_{dec} + 93_{dec}$ Schritt für Schritt durch.
```
  8 3 2
+   9 3

-------
```
$2 + 3 = 5$, also ist die nächste Ziffer `5` und der Übertrag $0$.
```
    8 3 2
+     9 3
      0
---------
        5
```
$3 + 9 + 0 = 12$, also ist die nächste Ziffer `2` und wir haben Übertrag $1$.
```
    8 3 2
+     9 3
    1 0
---------
      2 5
```
$8 + 1 = 9$, also ist die nächste Ziffer `9` und wir haben keinen Übertrag.
```
    8 3 2
+     9 3
  0 1 0
---------
    9 2 5
```
Die nächste Spalte enthält jetzt ausschließlich die $0$ aus dem Übertrag, die Rechnung ist also abgeschlossen.

Im Binärsystem wird exakt gleich gerechnet: Hat eine Spalte als Ergebnis einen Wert mindestens so groß wie die Basis (hier 2) wird die Basis abgezogen und eine 1 als Übertrag in die nächste Spalte geschrieben.
Wir rechnen als Beispiel $1011100_{bin} + 1101101_{bin}$.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1

-----------------
```
Die letzte Spalte ist addiert $0 + 1 = 1$, der Übertrag ist $0$.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
              0
-----------------
                1
```
Die vorletzte Spalte ergibt $0 + 0 + 0 = 0$ mit Übertrag $0$.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
            0 0
-----------------
              0 1
```
Die drittletzte Spalte ergibt $1 + 1 + 0 = 2$. Wir wissen $2_{dec} = 10_{bin}$, haben wir Übertrag $1$ und schreiben als drittletzte Ergebnisziffer `0`.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
          1 0 0
-----------------
            0 0 1
```
Die viertletzte Spalte ergibt $1 + 1 + 1 = 3$. Wir wissen $3_{dec} = 11_{bin}$, also haben wir erneut Übertrag $1$, jetzt ist aber auch die Ergebnisziffer eine `1`.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
        1 1 0 0
-----------------
          1 0 0 1
```
Jetzt haben wir schon alle Kombinationen gesehen. Mehr als $0$, $1$, $2$ oder $3$ kann nicht Ergebnis einer Spalte sein. Die nächste Spalte ist zusammenaddiert erneut $2$, also Übertrag $1$ und Ziffer `0`.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
      1 1 1 0 0
-----------------
        0 1 0 0 1
```
Und wieder ist $0 + 1 + 1 = 2$.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
    1 1 1 1 0 0
-----------------
      0 0 1 0 0 1
```
Und $1 + 1 + 1 = 3$.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
  1 1 1 1 1 0 0
-----------------
    1 0 0 1 0 0 1
```
Und den letzten Übertrag können wir einfach übernehmen, weil es keine Zahenstellen mehr zum dazuaddieren gibt.
```
    1 0 1 1 1 0 0
+   1 1 0 1 1 0 1
  1 1 1 1 1 0 0
-----------------
  1 1 0 0 1 0 0 1
```
Wer das Ergebnis verifizieren möchte, kann $1011100_{bin}$ und $1101101_{bin}$ erst ins Dezimalsystem umwandeln, dann die Addition durchführen und vergleichen mit $11001001_{bin}$ umgewandelt ins Dezimalsystem.


## Negative Zahlen

Bisher können wir nicht-negative ganze Zahlen in Binärform darstellen und sie addieren.
Der nächste Schritt ist zu überlegen, wie man mit negativen Zahlen rechnen könnte.
Am offentsichlichsten erscheint, ein extra Bit für das Vorzeichen zu verwenden: Ist das Bit $0$ sagen wir die Zahl ist positiv, ist das Bit $1$ sagen wir die Zahl ist negativ. Ein Nachteil dieses Ansatzes ist, dass die Addition zweier ganzer Zahlen dann eine Fallunterscheidung mit vier Fällen benötigt:
* beide Zahlen sind positiv
* die erste Zahl ist positiv und die zweite negativ
* die erste Zahl ist negativ und die zweite positiv
* beide Zahlen sind negativ.

Das ist etwas unelegant umzusetzen. Ein konzeptionell vielleicht noch größeres Problem ist allerdings ein anderes. $+0$ und $-0$ hätten in dieser Darstellung zwei unterschiedliche Bitmuster, obwohl es sich um die selbe Zahl handelt.

Stellen wir uns vor, dass wir das Vorzeichenbit direkt neben das wichtgste Zahlenstellenbit schreiben. Wenn man sich eine ganze Zahl im Speicher anguckt, muss man also nur das erste Bit lesen um das Vorzeichen zu erkennen. Die selbe Eigenschaft erhält man, wenn man negieren (also mal $-1$ rechen) einer Zahl definiert als das Umdrehen jedes einzelnen Bits: Aus jeder $1$ wird eine $0$ und andersherum. Wenn man immer einen Speicherbereich fester Größe für eine ganze Zahl reserviert und diese Größe mit entsprechend Puffer wählt, kann man immer davon ausgehen, dass die wichtigsten Bits der Zahl ungenutzt sind. Damit sind sie bei positiven Zahlen $0$ und bei negativen Zahlen $1$.
Das Problem mit der eindeutigen $0$ lösen wir, indem nach dem Umdrehen der Bits noch $1$ auf die gesamte Zahl addieren. Weil 
$$-0_{dec} = -0000\dots0000_{bin} = 1111\dots1111_{bin} + 1 = 0000\dots0000_{bin}$$
, wenn wir den letzen Übertrag ignorieren. Wie durch Magie funktioniert jetzt auch das Addieren zweier ganzer Zahlen mit dem selben Verfahren wie vorher, solange wir einfach den allerletzten Übertrag ignorieren. Diese Darstellung negativer ganzer Zahlen nennt sich Zweierkomplement und wird in jedem modernen Computer genutzt.


