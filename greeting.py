
#Tervitus
print("Tere tulemast programmi 'Tervitus'!")

surname = input("Mis on sinu perekonnanimi? ")
gender = input("Mis on sinu sugu? (m/n): ")

if gender == "m":
    print("Tere, härra " + surname + "!")
elif gender == "n":
    print("Tere, proua " + surname + "!")
else:
    print("Tere tulemast, " + surname + "!")

    
