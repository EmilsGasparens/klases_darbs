def summa(sk1,sk2):      # aisūta saņem
    rezultats=sk1+sk2
    return rezultats

def ievads():      #saņem
    skaitlis= int(input("Ievadi skaitli "))
    return skaitlis

def linija():     #neko nesūta , neko nesaņem
    print("******************")

def linija1(x):    #aizsūta , nesaņem
    for i in range(1,x):
        print("*")

skaitlis1=ievads()
skaitlis2=ievads()
linija()
rezul=summa(skaitlis1,skaitlis2)
print(rezul)
linija1(10)

skaitli_trešais=ievads()
skait=ievads()