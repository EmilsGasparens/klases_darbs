print("Četstūta laukuma apreiķināšana!")

while True:
    try:
        while True:
            garums=float(input("ievadi četstūra gatumu (cm): "))
            if garums<=0:
                print("Ievadiet pozitīvu skaitli")
            else:
                break
        while True:
            platums=float(input("ievadi četstūra platums (cm): "))
            if platums<=0:
                print("Ievadiet pozitīvu skaitli")
            else:
                break
        laukums=garums*platums
        print(f"Četrstūra laukums ir {laukums} cm2" )
        break
  
    except ValueError:
        print("nav ievadīts skaitlis")