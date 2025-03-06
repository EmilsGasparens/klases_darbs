# izveido programmu, kas ļau lietotājam parvaldīt klientu sarakstu.
#pievienot klientus, izdzēst, meklēt, parādīt visus klientus, iziet.
#i[klienti]
def paradit():
    vards=input("Ievadiet klienta vārdu:")
    klienti.append(vards.lower())
    print(f"klients{vards} ir pievienots")
def dzest_ierakstu(vards):
    if vards.upper() in klienti:
         klienti.remove(vards.lower())
         print(f"klients {vards} ir izdzēsts")
    else:
         print(f"klients {vards} nav sarakstā:")
def meklet_klientu(vards):
    skaits=0
    for kliemts in klienti:
        if vards.upper() ==klienti:
            skaits+=1
    if skaits>0:
        print(f"klients{vards} ir sastopams {skaits} reizes")
    else:
        print(f"klients {vards} nav sastopams")
  
def paradit_klientus():
    if klienti:
        print("Sarakste ir  sekojošie klienti:")
        for klients in klienti:
            print(klients)
    else:
        print("klientu saraksts ir tukšs")
    
klienti=[]
while True:
    print("izvēlieties darbību:")
    print("1-pievienot klientu")
    print("2-izdzēst klientu")
    print("3-meklet klientu")
    print("4-perādīt visus klientus")
    print("5-iziet")
    
    izvele=input("ievadiet izvēlēto darbību")
    
    if izvele=="1":
        paradit()
    elif izvele=="2":
        vards=input("Ievadit klienta vārdu dzēšanai:")
        dzest_ierakstu(vards)
    elif izvele=="3":
        vards=input("Ievadit klienta vārdu kuru vēlaties meklet")
        meklet_klientu(vards)
    elif izvele=="4":
       paradit_klientus()
        
    elif izvele=="5":
        print("programa beidz darbu")
        break
    else:
        print("nederīga izvēle, atkārtojiet")