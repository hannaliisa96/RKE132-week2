
""" #Veejoomise kalkulaator
#Alusta programmi.
#Väljasta programmi tervitus.
#Määra päevaseks veejoomise eesmärgiks 2000 ml ja salvesta see muutujasse goal.
#Küsi kasutajalt, mitu klaasi vett ta on täna joonud, ja salvesta vastus muutujasse glasses.
#Arvuta joodud vee kogus ja salvesta tulemus muutujasse water_intake.
#Arvuta täidetud päevanormi protsent ja salvesta tulemus muutujasse percent.
#Väljasta arvutatud protsent.
#Kui percent on väiksem kui 50, siis väljasta: "Alles poolel teel, joo edasi!".
#Muidu, kui percent on väiksem kui 100, siis väljasta: "Tubli, jätka samas vaimus!".
#Muidu väljasta: "Suurepärane, oled oma eesmärgi täitnud!".
#Lõpeta programm. """

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


