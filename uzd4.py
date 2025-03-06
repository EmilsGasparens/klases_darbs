#Masivs
numbers=[1,4,5,7]
''''
for numbers in range(4):
    num=int(input(f"Ievadiet {number+1} skaitli:"))
    numbers.append(num)
''' 
#print(f"Ievadiet skaitli {numbers}")
for number in range(4):
    print(f"{number[number]} ")
    
print(f"sarakstā ir {len(numbers)}")

skaitlis=10
numbers.append(skaitlis)
numbers[3]="Mājas"
del numbers(1)#izdzēš
numbers.pop(3)#izdzēš
numbers.remove(0)#izdzēš
print(numbers)
