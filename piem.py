# ir veiktas izmaias
valstis=["Igaunija","Latvija","Lietuva","polija"]

for i in valstis:
    print(i)
    
    
skaitli=[1,2,3,4,5,6,7,8,9,10]
skaitli=list(range(1,11))
for i in range(1,11):
    skaitli.append(i**2)
print(skaitli)

print(f"lielākais skaitlis ir:{max(skaitli)}")
print(f"Mazākais skaitlis ir:{min(skaitli)}")