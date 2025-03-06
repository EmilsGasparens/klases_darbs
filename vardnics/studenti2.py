#1 uzdevums
students={
    "vards":"Jānis",
    "uzvards":"Berziņš",
    "vecums":21,
    "kurss":3, 
}
print(f"sākotnējais saraksts{students}")
# 2uzdevums
students["vidējā atzīme"]=8.5
print(f"pēc papildināšanas saraksts{students}")
#3 uzdevums
students["vecums"]=students["vecums"]+1
students["kurss"]+=1
print(f"pēc izmaiņam saraksts{students}")
# 4 uzdevums
del students["uzvards"]
print(f"pēc dzēšanas saraksts{students}")
# 5 uzdevums
for key, value in students.items():
    print(f"{key}:{value}")
# 6 uzdevums
if "vidējā atzīme" in students:
    print(f"atslēga 'viējā atzīme'ir atrodama {students['vidējā atzīme']}")
else:
    print("atslēga 'vidējā atzīme' nav atrodama ")