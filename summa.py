#Dotajā saraksta [2,44,22,55,3,2,4,6,7] atrast visu skaitļu summu un reizinajumu.
#saraksts:dati, summa

saraksts=[2,44,22,55,3,2,4,6,7]
#summa
summa=0
for x in range(len(saraksts)):
    summa=summa+saraksts[x]
    
print(f"Saraksta skaitļu summa ir {summa}")
print(f"Saraksta skaitļu summa ir {sum(saraksts)}")

#reizināšana
reizinajums=1
for x in range(len(saraksts)):
    reizinajums=reizinajums*saraksts[x]
print(f"reizinājums ir {reizinajums} ")