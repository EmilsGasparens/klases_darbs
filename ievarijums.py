#Sieviete vēlas izvarīt ievarijumu no āboliem un ogām.
#Bet naudas ir tik cik ir.
#Sastadīt programu kura apreiķina cik daudz ievarijuma var izvarit
#Cik ir naudas
#cik daudz mums ir Aboli un cik ogas
#jazin recepte (cik būs ābolu , cik daudz ogas un cik daudz cukuru vaig uz vienu vienību)

def ievarijums(aboli, ogas, cukurs, cukura_cena):
    izmaksas=(aboli+ogas)*cukura_cena



aboli=float(input("Ievadiet ābolu daudzumu (kg)"))
ogas=float(input("Ievadiet ogu daudzumu (kg)"))
cukurs=float(input("cik cukura nepieciešams uz vienu kg"))
cukura_cena=float(input("ievadiet cukura cenu"))