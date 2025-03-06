import math

def saknes(a,b,c):
    D=b*b-4*a*c
    print(f"diskriminanta būs{D}")
    if D<0:
        print("kvadrātvienadojumam sakņu nav")
    elif D==0:
        x1=(-b+math.sqrt(D))/(2*a)
        print(f"kvadratvienadojumam ir viena sakne {x1}")
    else:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print(f"kvadrātvienadojuma saknes ir/n {x1} un {x2}")
def ievads():
    a=int(input("ievadi a skaitli "))
    b=int(input("ievadi b skaitli "))
    c=int(input("ievadi c skaitli ")) #D=b2−4ac.
    return a,b,c
print("Lai arpeiķinatu kvadratvienadojumu saknes ievadiet:")
while True:
    a,b,c=ievads()
    saknes(a,b,c)
    turpinat=input("vai velies turpināt? (Jā/Nē)")
    if turpinat =="Nē":
        print("Paldies par darbu!")
        break