
print("fakultaet von was?")
n = int(input())
fakultaet = 1
while n > 0:
    print("n = " + str(n) + ", fakultaet = " + str(fakultaet))
    fakultaet *= n # fakultaet = fakultaet * n
    n -= 1 #n = n - 1
print("ergebnis ist " + str(fakultaet))