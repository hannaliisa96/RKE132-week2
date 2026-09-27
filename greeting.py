
""" #Tervitus
#Alusta programmi.
#Väljasta ekraanile: "Tere tulemast programmi 'Tervitus'!".
#Küsi kasutajalt: "Mis on sinu perekonnanimi?".
#Salvesta vastus muutujasse surname.
#Küsi kasutajalt: "Mis on sinu sugu? (m/n): ".
#Salvesta vastus muutujasse gender.
#Kui gender on võrdne tähega "m", siis väljasta ekraanile: "Tere, härra [perekonnanimi]!".
#Muidu, kui gender on võrdne tähega "n", siis väljasta ekraanile: "Tere, proua [perekonnanimi]!".
#Muidu väljasta ekraanile: "Tere tulemast, [perekonnanimi]! (sugu ei olegi tähtis).".
#Lõpeta programm. """

print("Tere tulemast programmi 'Tervitus'!")

surname = input("Mis on sinu perekonnanimi? ")
gender = input("Mis on sinu sugu? (m/n): ")

if gender == "m":
    print("Tere, härra " + surname + "!")
elif gender == "n":
    print("Tere, proua " + surname + "!")
else:
    print("Tere tulemast, " + surname + "! (sugu ei olegi tähtis).")


