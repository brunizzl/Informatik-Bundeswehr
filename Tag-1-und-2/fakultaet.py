
print("fakultaet von was?")
n = int(input())
facultaet = 1
while n > 0:
    print("n = " + str(n) + ", facu = " + str(facultaet))
    facultaet *= n # facultaet = facultaet * n
    n -= 1 #n = n - 1
print("ergebnis ist " + str(facultaet))