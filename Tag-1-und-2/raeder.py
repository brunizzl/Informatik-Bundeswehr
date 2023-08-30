print("Mit wie vielen Rädern bist du heute hergekommen?")
raeder = int(input())
if raeder == 0:
    print("zu Fuß")
elif raeder == 1:
    print("Einrad")
elif raeder == 2:
    print("Motorrad oder Fahrrad")
    print("Hat den Fahrzeug ein Motor?")
    motor = input()
    if motor == "ja":
        print("Motorrad")
    elif motor == "nein":
        print("Fahrrad")
    else:
        print("Du hättest \"ja\" oder \"nein\" schreiben müssen.")        
elif raeder == 3:
    print("Dreirad")
elif raeder == 4:
    print("Auto")
else:
    print("Bahn")
