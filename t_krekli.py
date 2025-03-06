def pasutijums(skaits, apdruka, piegade):
    if apdruka.lower()=="teksts":
        cena=5
    elif apdruka.lower()=="zīme":
        cena=10
    elif apdruka.lower()=="foto":
        cena=20
    else:
        return f"Nav noradīts pareizs apdrukas veids"
    
    summa=skaits*cena
    
    if piegade==True and summa<30:
        summa +=5
    if summa>=50:
        summa *0,95
        
    return f"{skaits}T-krekli ar apdruku {apdruka} maksa {summa} EUR"
    
    
    
skaits=int(input("cik kreklus pasutīsiet?"))
apdruka=input("Īzvēlieties apdrukas veidu(Teksts;Zīme:Foto)")
piegade=bool(input("Vai vaidzēs piegadi?(True/False)"))

print(pasutijums(skaits, apdruka, piegade))