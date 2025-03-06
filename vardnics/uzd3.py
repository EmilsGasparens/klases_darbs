a={
    "vards":"Jānis",
    "uzvards":"Berziņš",
    "klase":12,
    "vecums":19
}
b={"iela":"Rīga","māja":24}

print(a)
print(len(a))
print(list(a.keys()))

print(b['iela'])
print(a["uzvards"])
print(f"vards: {a['vards']}, uzvards: {a['uzvards']} macas {a['klase']}.klasē")

a["vecums"]=20
print(a)

for i in a.keys():
    print(f"key: {i}, value:{a[i]}")
    
if "Pēteris "in a:
    print("Pēteris ir vardnīcs")
else:
    print("Pēteros nav vērdnīca ")

c={}
c['stunda']='Pirmā'
c['laiks']='8:00'
print(c)
#del vai pop
del c["laiks"]
print(c)
c.pop('stunda')
print(c)