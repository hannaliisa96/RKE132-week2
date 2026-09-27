
#Veejoomise kalkulaator

print("Tere tulemast programmi 'Veejoomise kalkulaator'!")

goal = 2000
glasses = int(input("Mitu klaasi vett oled täna joonud? "))

water_intake = glasses * 250
percent = (water_intake/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, joo edasi!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma eesmärgi täitnud!")


