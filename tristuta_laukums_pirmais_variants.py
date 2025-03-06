print("tistura laukuma apreiķināšana!")

while True:
    try:
        while True:
            pamatagarums=float(input("ievadi tristūta pamata gatumu no kuta ir novilkts aukstums (cm): "))
            if pamatagarums<=0:
                print("Ievadiet pozitīvu skaitli")
            else:
                break
        while True:
            aukstumagarums=float(input("ievadi tristuta aukstumu (cm): "))
            if aukstumagarums<=0:
                print("Ievadiet pozitīvu skaitli")
            else:
                break
        laukums=(pamatagarums*aukstumagarums)/2
        print(f"tistuta  laukums ir {laukums} cm2" )
        break
  
    except ValueError:
        print("nav ievadīts skaitlis")