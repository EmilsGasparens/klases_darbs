print("Cetru darbību kalkalatots")
print("Izvelieties darbību:")   
print("1-saskaitīšana(+)")
print("2- atņemšana(-)")
print("3-reizinašana(*)")
print("4-dalīšaana(/)")

izvele=input("izvēlies darbību munuru(1,2,3,4)")
if izvele in ('1','2','3','4'):
    while True:
        try:
            skaitlis1=float(input("Ievadiet pirmo skaitli"))
            skaitlis2=float(input("Ievadiet otro skaitli"))
            break
        except ValueError:
            print("Nepateiza ievade! Jāievada skaitli")
        

    
    if izvēle=="1":
        rezultats=skaitlis1+skaitlis2
        print(f"{skaitlis1}+{skaitlis2}={rezultats}")
    elif izvēle=="2":
        rezultats=skaitlis1+skaitlis2
        print(f"{skaitlis1}-{skaitlis2}={rezultats}")
    elif izvēle=="3":
        rezultats=skaitlis1+skaitlis2
        print(f"{skaitlis1}*{skaitlis2}={rezultats}")
    elif izvēle=="4":
        if skaitlis2==0:
            print("Kļūda: Dalīsana ar nūlu nav atļauta.")
        else:
            rezultats=skaitlis1+skaitlis2
            print(f"{skaitlis1}/{skaitlis2}={rezultats}")
else:
    print("Nepareiza izvēle meiģīni velreiz")