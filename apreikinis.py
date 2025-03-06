import math
def gridas_izmaksas(platums, garums, cena, linoleja_platums):
    laukums=math.ceil(platums)*math.ceil(garums)
    izmaksas=laukums*cena/linoleja_platums
    return izmaksas



platums=float(input("Ievadiet iztabas platumu(m)"))
garums=float(input("Īevadiet iztabas garumu(m)"))
cena=float(input("Ievadi linoleja cenu(eur/m2)"))
linoleja_platums=float(input("Ievadi linoleja platumu (m)"))


print("Klājot garumā")
izmaksas=gridas_izmaksas(platums, garums, cena, linoleja_platums)
print(f"Grīdas izmaksas ir{round(izmaksas,2)}")
print("klājotr pltumā")
izmaksas=gridas_izmaksas(garums, platums, cena, linoleja_platums)
print(f"Grīdas izmaksas ir{round(izmaksas,2)}")