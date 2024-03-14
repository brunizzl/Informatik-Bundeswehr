
## Nachkommastellen

Im Dezimalsystem hat eine beliebige Ziffer einer Zahl ein zehntel der Wichtigkeit der Ziffer direkt links daneben. 
Etwa hat in $`15678_{dec}`$ die Ziffer $7$ Gewicht $10$. Die Ziffer links davon ist $6$ mit Gewicht $100$. In $15678$ ist also $6$ zehn Mal so wichtig wie $7$.

Dieses Muster hält auch für Nachkommastellen. In $`15678.9_{dec}`$ hat $8$ die Wichtigkeit $1$, $9$ hat nur noch die Wichtigkeit von einem Zehntel. 

Im Binärsystem hat eine beliebige Ziffer einer Zahl die Hälfte der Wichtigkeit der Ziffer direkt links daneben. 
Auch hier hält das Muster für Nachkommastellen. 

Binärdarstellung | Dezimaldarstellung
-----------------|-------------------
$\vdots$         | $\vdots$
$10000$          | $`2^4 = 16`$
$1000$           | $`2^3 = 8`$
$100$            | $`2^2 = 4`$
$10$             | $`2^1 = 2`$
$1$              | $`2^0 = 1`$
$0.1$            | $`2^{-1} =\frac 1 2 = 0.5`$
$0.01$           | $`2^{-2} =\frac 1 4 = 0.25`$
$0.001$          | $`2^{-3} =\frac 1 8 = 0.125`$
$0.0001$         | $`2^{-4} =\frac 1 {16} = 0.0625`$
$\vdots$         | $\vdots$

Als Beispiel konvertieren wir die Zahl $`1010.0101_{bin}`$ ins Dezimalsystem.

$`1010.0101_{bin} = 2^3 + 2^1 + 2^{-2} + 2^{-4} = 2^3 + 2^1 + \frac 1 4 + \frac 1 {16}`$

$`= 8 + 2 + 0.25 + 0.0625 = 10.3125`$

Die andere Richtung funktioniert analog. Haben wir eine Zahl im Dezimalsystem, etwa $`23.75_{dec}`$, müssen wir sie in eine Summe von Zweierpotenzen zerlegen um ihre Binärform zu erhalten:

$`23.75_{dec} = 16 + 4 + 2 + 1 + 0.5 + 0.25 = 16 + 4 + 2 + 1 + \frac 1 2 + \frac 1 4 = 2^4 + 2^2 + 2^1 + 2^0 + 2^{-1} + 2^{-2}`$

Die einsen von $`23.75_{dec}`$ befinden sich also an den Positionen $4, 2, 1, 0, -1$ und $-2$.
Alle nicht-negativen Positionen sind links vom Dezimalpunkt aufgeführt, die negativen rechts davon:

$`23.75_{dec} = 10111.11_{bin}`$

Manchmal haben wir bei Umwandlungen in dieser Richtung allerdings weniger Glück:

$`1.2_{dec} = 1 + 0.125 + 0.0625 + 0.0078125 + 0.00390625 + 0.00048828125 + 0.000244140625 + \dots`$

Das Problem tritt auf, wenn unsere Zahl nicht als Bruch geschrieben werden kann, dessen Nenner eine Zweierpotenz ist. 
Bei $`23.75_{dec}`$ hatten wir Glück, denn $`23.75_{dec} = \frac{95}{4}`$ und $`4 = 2^2`$. Dagegen ist $`1.2_{dec} = \frac{12}{10} = \frac{6}{5}`$. Egal mit welcher ganzen Zahl wir diesen Bruch erweitern, der Nenner wird immer durch $5$ teilbar bleiben. Es ist allerdings keine Zweierpotenz durch $5$ teilbar. Das selbe Problem tritt im Dezimalsystem auf, wenn wir ein Bruch haben, dessen Nenner nicht zu einer Zehnerpotenz erweitert werden kann. Deshalb hat zum Beispiel $`\frac 1 7`$ im Dezimalsystem unendlich viele Nachkommastellen.

Dementsprechend hässlicher ist die Umwandlungstabelle von Dezimal nach Binär:

Dezimaldarstellung | Binärdarstellung
-------------------|-------------------
$\vdots$           | $\vdots$
$100$              | $`64 + 32 + 4 = 110010_{bin}`$
$10$               | $`8 + 2 = 1001_{bin}`$
$1$                | $`1 = 1_{bin}`$
$0.1$              | $`0.00011001100110011001100110011001\dots`$
$0.01$             | $`0.00000010100011110101110000101000\dots`$
$0.001$            | $`0.00000000010000011000100100110111\dots`$
$\vdots$           | $\vdots$


## Wissentschaftliche Notation

In der Regel ist ein Zahlenwert nur bis zu einer gewissen Genauigkeit wichtig. Etwa interessiert es beim Bau eines Hauses in der Regel keinen der Beteiligten, ob das Fundament $`105.2 m^3`$ Beton oder $`105.2 m^3 \cdot 1.000001 = 105.2001052 m^3`$ benötigt. So genau wird der Betonlaster ohnehin nicht befüllt und so genau sind auch die Berechnungen der Betonmenge gar nicht. 

Wirklich relevant sind also nur die ersten paar Stellen einer Zahl ab der ersten Stelle die nicht `0` ist. Guckt man also nur auf die ersten vier _signifikanten_ Stellen von $`105.2`$ und $`105.2001052`$, sind beide Zahlen identisch. Nicht einfach immer bis zur -sagen wir dritten- Nachkommastelle zu runden ist wichtig, weil wir in einem allgemeinen Kontext nicht wissen in welcher Größenordnung sich eine Zahl befindet. Für das Betonvolumen mag das noch halbwegs passen, aber das Gewicht eines Zahnrades in einem Uhrenwerk, sagen wir $`0.000067145 \text{kg}`$ wäre damit auf $0 \text{kg}$ gerundet. Wen auch immer dieses Gewicht interessiert, mit $0$ wird sich diese Person dann nicht zufrieden geben.

Die sogenannte _wissentschaftliche Notation_ formalisiert diese Idee. Zum einen werden immer nur die wichtigsten paar Stellen einer Zahl aufgeschrieben -sagen wir vier-, zum anderen wird man unnötige Nullen an Anfang bzw. Ende der Zahl los, indem man sie so oft durch 10 teilt oder mal 10 nimmt, bis die Zahl zwischen 1 und 10 liegt. Den extra Faktor schreibt man danach als $`10^n`$ dahinter.

Beispiele:
* Die Lichtgeschwindigkeit im Vaakuum beträgt etwa $`299700000 \frac m s = 2.997 \cdot 10^8 \frac m s`$.
* Die Ladung eines Elektron beträgt etwa $`-0.000000000000000001602 \text C = -1.602 \cdot 10^{-19} \text C`$.
* Die Avogadrozahl ist etwa $`602200000000000000000000 \frac 1 {\text{mol}} = 6.022 \cdot 10^{23} \frac 1 {\text{mol}}`$.

## Fließkommazahlen

Fließkommazahlen nutzen wissentschaftliche Notation, aber in Binär. Heutige Computer nutzen dabei quasi alle den selben Standard, nämlich [IEEE 754](https://de.wikipedia.org/wiki/IEEE_754).

Als Beispiel listen wir hier auf, wie die $64$ Bit des Formates `binary64` genutzt sind.
* Ein Bit repräsentiert das Vorzeichen: `0` bedeutet positiv, `1` negativ.
* $52$ Bit sind die signifikanten Stellen der Zahl.
* $11$ Bit speichern den Exponenten.

Allgemein hat eine Fließkommazahl im `binary64` Format also die Form

$`(-1)^b \cdot m \cdot 2^e`$

wobei $b$ das Vorzeichenbit repräsentiert, $m$ die ersten $52$ signifikanten Stellen und $e$ den Exponenten.
Unsere Zahl $`23.75_{dec} = 10111.11_{bin}`$ würden wir also schreiben als

$`(-1)^0 \cdot 1.011111_{bin} \cdot 2^{4} = (-1)^0 \cdot 1.011111_{bin} \cdot 2^{100_{bin}}`$. 
