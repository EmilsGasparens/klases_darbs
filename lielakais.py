#Dotajā saraksta [2,44,22,55,3,2,4,6,7] atrast lielako skaitli.
#saraksts:dati, lielakais: max

saraksts=[2,44,22,55,3,2,4,6,7]

max=max(saraksts)
print(f"Lielākais skaitlis ir {max}")

max=saraksts[0]
for x in range(len(saraksts)):
    if max<saraksts[x]:
           max=saraksts[x]
           
print(f"Lielākais skaitlis ir {max}")
