
# benutze dinge aus der datei "zufall.py" im selben ordner
# nenne diese sammlung von dingen "zufall"
import zufall

# benutze dinge aus datei "blatt08.py" im selbem ordner
# nenne diese sammlung von dingen "sort"
import blatt08 as sort

# benutze die "time" bibliothek, die direkt mit python inbegriffen ist
# nenne diese sammlung von dingen "time"
import time

# benutze dinge aus externer bibliothek "matplotlib.pyplot" 
# nenne diese sammlung von dingen "plt"
# vorsicht: das funktioniert nur, wenn die bibliothek auch installiert ist.
import matplotlib.pyplot as plt

# benutze dinge aus datei "testdatei" in unterordner "testordner"
import testordner.testdatei

# beispiel von nutzung eines dings aus datei "testdatei" in unterordner "testordner"
print(testordner.testdatei.test)


## teste die laufzeit von bubblesort vs mergesort

# wenn i ein index in laengen ist, sagt "bubble_zeiten[i]", 
# wie lange es gedauert hat eine liste mit 
# "laengen[i]" vielen eintraegen mit bubblsort zu sortieren.
# selbes prinzip gilt fuer merge_zeiten und mergesort.
laengen = []
bubble_zeiten = []
merge_zeiten = []

for n in range(20, 45):
    laenge = int(1.2 ** n)
    print("n:", n, "laenge:", laenge)
    
    # generiere zufaellige liste in zweifacher ausfuerung
    x1 = zufall.zufaellige_liste(laenge)
    laengen.append(laenge)
    x2 = x1.copy()
    
    # sortiere eine ausfuerung der generierten liste mut bubblesort
    # und messe wie lange es dauert bis bubblesort fertig ist
    print("bubblesort...")
    bubble_start = time.perf_counter()
    sort.bubblesort(x1)
    bubble_fertig = time.perf_counter()
    bubble_zeit = bubble_fertig - bubble_start
    bubble_zeiten.append(bubble_zeit)
    print("fertig:", x1[:5], "...", x1[(laenge - 5):], 
        "in", bubble_zeit, "sekunden")
    
    # sortiere eine ausfuerung der generierten liste mut mergesort
    # und messe wie lange es dauert bis mergesort fertig ist
    print("mergesort...")
    merge_start = time.perf_counter()
    x3 = sort.mergesort(x2)
    merge_fertig = time.perf_counter()
    merge_zeit = merge_fertig - merge_start
    merge_zeiten.append(merge_zeit)
    print("fertig:", x3[:5], "...", x3[(laenge - 5):], 
        "in", merge_zeit, "sekunden")
    
    print()

# dieser part funktioniert nur, wenn matplotlib installiert ist.
plt.figure()
plt.grid()
plt.plot(laengen, bubble_zeiten, "r")
plt.plot(laengen, merge_zeiten, "b")
plt.show()
