'''
print("Esi sveiks!")
skaitlis=input("ievadiet skaitli ")
print(f"ievadītais skaitlis ir {skaitlis}")
'''
pirmais_skaitlis=int(input("ievadi pirmo skaitli "))
otrais_skaitlis=int(input("ievadi otro skaitli "))
summa=pirmais_skaitlis+otrais_skaitlis
print(f"Skaitļu {pirmais_skaitlis} un {otrais_skaitlis} summa ir {summa}")


if pirmais_skaitlis>otrais_skaitlis:
    print("pirmais skaitlis ir lielāks ")
elif pirmais_skaitlis<otrais_skaitlis:
    print("otrais skaitlis ir lielāks")
else:
    print("skaitļi ir vienādi")