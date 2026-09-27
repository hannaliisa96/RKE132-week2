#Alusta programmi.
#Küsi kasutajalt: "Mis päev on homme? (tööpäev/puhkepäev)".
#Salvetsa vastus muutujasse day.
#Kui day on võrdne sõnaga "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!".
#Muidu, kui day on võrdne sõnaga "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist".
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Vale väärtus".
#Lõpeta programm.))"

""" day = input("Mis päev on homme? (tööpäev/puhkepäev): ")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist")
else:
    print("Vale väärtus") """



""" 
#Finantsnõustaja
print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul on praegu? "))

if money < 2500:
    print("Sul pole piisvalt raha. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta uus iPhone 17  pro sularahas!")
else:
    print("Saad osta iPhone 17 pro ja veel jääb raha üle.")
     """


#Sammulugeja
goal = 10000
steps = int(input("Mitu sammu oled juba teinud?: "))

percent = (steps/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")

