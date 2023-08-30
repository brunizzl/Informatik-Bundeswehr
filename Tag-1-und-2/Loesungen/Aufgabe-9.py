print("Gebe eine Zahl ein")
zahl = int(input())
if zahl % 7 == 0: #rest bei teilen durch 7 ist 0 -> zahl ist durch  teilbar
    geteilt = zahl // 7 #// für int ergebnis
    print(str(zahl) + " ist exakt " + str(geteilt) + " mal 7.")
else:
    print(str(zahl) + " kann nicht glatt durch 7 geteilt werden.")

wurzel = zahl ** 0.5
if int(wurzel) ** 2 == zahl: #mit int verliert wurzel nachkommastellen
    print(str(zahl) + " ist eine Quadratzahl (mit Wurzel " + str(int(wurzel)) + ")")
else:
    print(str(zahl) + " ist keine Quadratzahl.")