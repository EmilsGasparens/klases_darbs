saraksts=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    saraksts.append(i**2)
print(saraksts)

a=min(saraksts)
print("mazākais skaitkis ir",(a))
b=max(saraksts)
print("lielākais skaitlis ir",(b))

